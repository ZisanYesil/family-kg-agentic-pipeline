# Triple matching report: 873

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Secrets_of_a_Door_to_Door_Salesman | hasCreator | Wolf_Rilla |
| Secrets_of_a_Door_to_Door_Salesman | hasDirector | Wolf_Rilla |
| Secrets_of_a_Door_to_Door_Salesman | type | Artifact |
| Secrets_of_a_Door_to_Door_Salesman | type | CreativeWork |
| Secrets_of_a_Door_to_Door_Salesman | type | Film |
| Wolf_Rilla | type | Agent |
| Wolf_Rilla | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| United_Kingdom | type | Country |
| United_Kingdom | type | Place |
| Wolf_Rilla | hasCountry | United_Kingdom |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Wolf_Rilla | hasCountry | country_germany |
| country_germany | type | Country |
| country_germany | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 13 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.700000 |
| Recall | 0.700000 |
| F1 score | 0.700000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
