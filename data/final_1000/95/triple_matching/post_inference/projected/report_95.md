# Triple matching report: 95

# 1. Matched triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Indian | type | Country |
| Indian | type | Place |
| Kalloori_Vaasal | hasCreator | Pavithran |
| Kalloori_Vaasal | hasDirector | Pavithran |
| Kalloori_Vaasal | type | Artifact |
| Kalloori_Vaasal | type | CreativeWork |
| Kalloori_Vaasal | type | Film |
| Lakshmi_s_NTR | hasCreator | Ram_Gopal_Varma |
| Lakshmi_s_NTR | hasDirector | Ram_Gopal_Varma |
| Lakshmi_s_NTR | type | Artifact |
| Lakshmi_s_NTR | type | CreativeWork |
| Lakshmi_s_NTR | type | Film |
| Pavithran | type | Agent |
| Pavithran | type | Person |
| Ram_Gopal_Varma | hasCountry | Indian |
| Ram_Gopal_Varma | type | Agent |
| Ram_Gopal_Varma | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Pavithran_Tamil_film_director | hasCountry | Indian |
| Pavithran_Tamil_film_director | type | Agent |
| Pavithran_Tamil_film_director | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pavithran | hasCountry | Indian |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 20 |
| Union triples in scope | 21 |
| True positives (matched) | 17 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.944444 |
| Recall | 0.850000 |
| F1 score | 0.894737 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
