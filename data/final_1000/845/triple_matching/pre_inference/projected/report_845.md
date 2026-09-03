# Triple matching report: 845

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Monsieur_N | hasDirector | Antoine_de_Caunes |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Antoine_de_Caunes | hasChild | Emma_de_Caunes |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Antoine_de_Caunes | type | Person |
| Antoine_de_Caunes | type | NamedIndividual |
| Antoine_de_Caunes | label | "Antoine de Caunes" |
| Emma_de_Caunes | hasParent | Antoine_de_Caunes |
| Emma_de_Caunes | type | Person |
| Emma_de_Caunes | type | NamedIndividual |
| Emma_de_Caunes | label | "Emma de Caunes" |
| Monsieur_N | type | Film |
| Monsieur_N | type | NamedIndividual |
| Monsieur_N | label | "Monsieur N." |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
