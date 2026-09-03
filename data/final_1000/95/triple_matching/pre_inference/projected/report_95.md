# Triple matching report: 95

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Kalloori_Vaasal | hasDirector | Pavithran |
| Lakshmi_s_NTR | hasDirector | Ram_Gopal_Varma |
| Ram_Gopal_Varma | hasCountry | Indian |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pavithran_Tamil_film_director | hasCountry | Indian |

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Indian | type | Country |
| Indian | type | NamedIndividual |
| Indian | label | "India" |
| Indian | altLabel | "Indian" |
| Kalloori_Vaasal | type | Film |
| Kalloori_Vaasal | type | NamedIndividual |
| Kalloori_Vaasal | label | "Kalloori Vaasal" |
| Lakshmi_s_NTR | type | Film |
| Lakshmi_s_NTR | type | NamedIndividual |
| Lakshmi_s_NTR | label | "Lakshmi's NTR" |
| Pavithran | hasCountry | Indian |
| Pavithran | type | Person |
| Pavithran | type | NamedIndividual |
| Pavithran | label | "Pavithran" |
| Ram_Gopal_Varma | type | Person |
| Ram_Gopal_Varma | type | NamedIndividual |
| Ram_Gopal_Varma | label | "Ram Gopal Varma" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 21 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.150000 |
| Recall | 0.750000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
