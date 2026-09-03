# Triple matching report: 269

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Isaac_Schwartz | hasDeathPlace | Siversky |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Straw_Hat | hasComposer | Isaac_Schwartz |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Isaac_Schwartz | type | Person |
| Isaac_Schwartz | type | NamedIndividual |
| Isaac_Schwartz | label | "Isaac Schwartz" |
| Isaac_Schwartz | altLabel | "Isaac Iosifovich Schwartz" |
| Siversky | type | Place |
| Siversky | type | NamedIndividual |
| Siversky | label | "Siversky" |
| Siversky | altLabel | "Siversky, near Saint Petersburg, Russian Federation" |
| The_Straw_Hat | type | Film |
| The_Straw_Hat | type | NamedIndividual |
| The_Straw_Hat | label | "The Straw Hat" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
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
