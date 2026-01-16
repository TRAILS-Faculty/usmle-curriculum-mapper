import json
from sentence_transformers import SentenceTransformer, util

_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with open("data/usmle_hierarchical_keywords.json") as f:
    _usmle = json.load(f)["USMLE"]

_flat = []
for cat, items in _usmle.items():
    _flat.extend(items)

_emb = _model.encode(_flat, convert_to_tensor=True)


def expand_keywords(sentence):
    s_emb = _model.encode(sentence, convert_to_tensor=True)
    scores = util.cos_sim(s_emb, _emb)[0]
    topk = scores.topk(3).indices
    return list({ _flat[int(i)] for i in topk })
