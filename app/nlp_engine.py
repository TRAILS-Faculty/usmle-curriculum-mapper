import pdfplumber
import pandas as pd
import re
from nltk.tokenize import sent_tokenize
from semantic_expander import expand_keywords
from competency_classifier import classify_sentence
from embedding_index import semantic_match

LEARNING_HEADERS = re.compile(r"^\s*(learning\s+objectives?|objectives?)", re.IGNORECASE)

def extract_pages(file):
    pages = []
    with pdfplumber.open(file) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            pages.append({"index": i+1, "text": text})
    return pages

def find_objectives_blocks(pages):
    objs = []
    for p in pages:
        lines = (p["text"] or "").splitlines()
        for j, line in enumerate(lines):
            if LEARNING_HEADERS.search(line.strip()):
                block = "
".join(lines[j:j+20])
                objs.append({"page": p["index"], "text": block})
    return objs

def analyze_pdf(uploaded_pdf):
    pages = extract_pages(uploaded_pdf)
    text = "
".join([p["text"] for p in pages])
    sentences = [s.strip() for s in sent_tokenize(re.sub(r"\s+"," ", text)) if s.strip()]
    df = pd.DataFrame({"sentence": sentences})

    # Learning objective flag per sentence window (simple heuristic)
    objectives = find_objectives_blocks(pages)
    objectives_text = "

".join([o["text"] for o in objectives]) if objectives else ""

    df["expanded_keywords"] = df["sentence"].apply(expand_keywords)
    df["competency"] = df["sentence"].apply(classify_sentence)
    df["organ_system"] = df["sentence"].apply(semantic_match)
    df["in_objectives"] = df["sentence"].apply(lambda s: bool(re.search(r"learning objectives|objective", s, re.I)))

    # Summarize coverage by keyword (count + objectives rule)
    summary = df.explode("expanded_keywords").groupby("expanded_keywords").size().reset_index(name="Mentions")
    def coverage(row):
        # simplistic: if any sentence marked objectives contains keyword
        in_obj = bool(re.search(re.escape(row["expanded_keywords"]), objectives_text, re.I)) if objectives_text else False
        if in_obj or row["Mentions"] >= 10:
            return "Extensive"
        if 3 <= row["Mentions"] <= 9:
            return "Moderate"
        if row["Mentions"] in (1,2):
            return "Low"
        return "Not Covered"
    summary["Coverage"] = summary.apply(coverage, axis=1)
    return df, summary.sort_values(["Coverage","Mentions"], ascending=[True, False])
