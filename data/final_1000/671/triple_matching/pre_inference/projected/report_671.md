# Triple matching report: 671

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Baree_Son_of_Kazan | hasDirector | David_Smith |
| David_Smith | hasDeathPlace | Santa_Barbara_California |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Baree_Son_of_Kazan | type | Film |
| Baree_Son_of_Kazan | type | NamedIndividual |
| Baree_Son_of_Kazan | label | "Baree, Son Of Kazan (1918 film)" |
| David_Smith | type | Person |
| David_Smith | type | NamedIndividual |
| David_Smith | label | "David Smith" |
| Santa_Barbara_California | type | Place |
| Santa_Barbara_California | type | NamedIndividual |
| Santa_Barbara_California | label | "Santa Barbara, California" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
