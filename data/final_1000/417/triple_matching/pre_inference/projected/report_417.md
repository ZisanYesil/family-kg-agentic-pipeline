# Triple matching report: 417

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Catalpa_Farm | hasCountry | United_States |
| Temple_Adath_Israel_Owensboro_Kentucky | hasCountry | United_States |

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
| Catalpa_Farm | type | Artifact |
| Catalpa_Farm | type | NamedIndividual |
| Catalpa_Farm | label | "Catalpa Farm" |
| Temple_Adath_Israel_Owensboro_Kentucky | type | Artifact |
| Temple_Adath_Israel_Owensboro_Kentucky | type | NamedIndividual |
| Temple_Adath_Israel_Owensboro_Kentucky | label | "Temple Adath Israel (Owensboro, Kentucky)" |
| Temple_Adath_Israel_Owensboro_Kentucky | altLabel | "Temple Adath Israel" |
| United_States | type | Country |
| United_States | type | NamedIndividual |
| United_States | label | "United States" |

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
