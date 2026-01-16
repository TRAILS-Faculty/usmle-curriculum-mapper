import json
from sentence_transformers import SentenceTransformer, util

_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with open("data/usmle_keyword_sets.json") as f:
    _ks = json.load(f)
_topics = _ks["Organ_Systems"]
_emb = _model.encode(_topics, convert_to_tensor=True)

def semantic_match(sentence: str) -> str:
    s_emb = _model.encode(sentence, convert_to_tensor=True)
    scores = util.cos_sim(s_emb, _emb)[0]
    idx = int(scores.topk(1).indices[0])
    return _topics[idx]
