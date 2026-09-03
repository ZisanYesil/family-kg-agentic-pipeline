# Triple matching report: 873

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Secrets_of_a_Door_to_Door_Salesman | hasDirector | Wolf_Rilla |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Wolf_Rilla | hasCountry | United_Kingdom |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Secrets_of_a_Door_to_Door_Salesman | type | Film |
| Secrets_of_a_Door_to_Door_Salesman | type | NamedIndividual |
| Secrets_of_a_Door_to_Door_Salesman | label | "Secrets of a Door-to-Door Salesman" |
| Wolf_Rilla | hasCountry | country_germany |
| Wolf_Rilla | type | Person |
| Wolf_Rilla | type | NamedIndividual |
| Wolf_Rilla | label | "Wolf Rilla" |
| country_germany | type | Country |
| country_germany | type | NamedIndividual |
| country_germany | label | "Germany" |
| country_germany | altLabel | "German" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
