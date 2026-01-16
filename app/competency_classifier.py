_RULES = {
    "Patient Care: Diagnosis": ["diagnosis","workup","test","imaging","lab"],
    "Patient Care: Management": ["management","treatment","therapy","dose","rx","antibiotic"],
    "Medical Knowledge/Scientific Concepts": ["pathogenesis","mechanism","molecular","cellular","virulence","pharmacodynamics","pharmacokinetics"],
    "Communication & Interpersonal Skills": ["counsel","discuss","shared decision","informed consent"],
    "Professionalism": ["ethic","confidential","consent","professional"],
    "Systems-Based Practice": ["patient safety","quality","handoff","system"],
    "Practice-Based Learning & Improvement": ["evidence","literature","biostatistics","confidence interval","odds ratio"],
}

def classify_sentence(sentence: str) -> str:
    s = sentence.lower()
    for comp, keys in _RULES.items():
        if any(k in s for k in keys):
            return comp
    return "General"
