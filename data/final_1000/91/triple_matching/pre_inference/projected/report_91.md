# Triple matching report: 91

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gunsmoke | hasDirector | Nathan_Juran |
| Nathan_Juran | hasBirthPlace | Gura_Humorului |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Gunsmoke | type | Film |
| Gunsmoke | type | NamedIndividual |
| Gunsmoke | label | "Gunsmoke (film)" |
| Gura_Humorului | type | Place |
| Gura_Humorului | type | NamedIndividual |
| Gura_Humorului | label | "Gura Humorului" |
| Nathan_Juran | type | Person |
| Nathan_Juran | type | NamedIndividual |
| Nathan_Juran | label | "Nathan Juran" |
| Nathan_Juran | altLabel | "Naftuli \"Nathan\" Hertz Juran" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
