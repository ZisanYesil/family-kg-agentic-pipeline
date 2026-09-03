# Triple matching report: 488

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Stefan_Vladislav | hasParent | Stefan_the_First_Crowned |
| Stefan_the_First_Crowned | hasCountry | Serbian_Grand_Principality |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Stefan_Vladislav | type | Person |
| Stefan_Vladislav | type | NamedIndividual |
| Stefan_Vladislav | label | "Stefan Vladislav" |
| Stefan_the_First_Crowned | hasCountry | serbia |
| Stefan_the_First_Crowned | hasParent | Stefan_Vladislav |
| Stefan_the_First_Crowned | type | Person |
| Stefan_the_First_Crowned | type | NamedIndividual |
| Stefan_the_First_Crowned | label | "Stefan the First-Crowned" |
| Stefan_the_First_Crowned | altLabel | "Stefan Nemanjić" |
| serbia | type | Country |
| serbia | type | NamedIndividual |
| serbia | label | "Serbia" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
