# Triple matching report: 500

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jeff_Celentano | hasBirthPlace | Pemberton_New_Jersey |
| Say_it_in_Russian | hasDirector | Jeff_Celentano |

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
| Jeff_Celentano | type | Person |
| Jeff_Celentano | type | NamedIndividual |
| Jeff_Celentano | label | "Jeff Celentano" |
| Jeff_Celentano | altLabel | "Jeff Weston" |
| Pemberton_New_Jersey | type | Place |
| Pemberton_New_Jersey | type | NamedIndividual |
| Pemberton_New_Jersey | label | "Pemberton, New Jersey" |
| Say_it_in_Russian | type | Film |
| Say_it_in_Russian | type | NamedIndividual |
| Say_it_in_Russian | label | "Say it in Russian" |

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
