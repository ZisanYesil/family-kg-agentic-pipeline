# Triple matching report: 458

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| A_Summer_You_Will_Never_Forget | hasCountry | German |
| Alfred_von_Ingelheim_s_Dramatic_Life | hasCountry | German |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| A_Summer_You_Will_Never_Forget | type | Film |
| A_Summer_You_Will_Never_Forget | type | NamedIndividual |
| A_Summer_You_Will_Never_Forget | label | "A Summer You Will Never Forget" |
| Alfred_von_Ingelheim_s_Dramatic_Life | type | Film |
| Alfred_von_Ingelheim_s_Dramatic_Life | type | NamedIndividual |
| Alfred_von_Ingelheim_s_Dramatic_Life | label | "Alfred von Ingelheim's Dramatic Life" |
| German | type | Country |
| German | type | NamedIndividual |
| German | label | "Germany" |
| German | altLabel | "German" |
| German | altLabel | "West German" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
