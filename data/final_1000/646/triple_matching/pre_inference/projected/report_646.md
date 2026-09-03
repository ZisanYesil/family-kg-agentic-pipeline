# Triple matching report: 646

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Only_When_I_Dance | hasPublicationDate | "2009"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Wicked_Dreams_of_Paula_Schultz | hasPublicationDate | "1968"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Only_When_I_Dance | type | Film |
| Only_When_I_Dance | type | NamedIndividual |
| Only_When_I_Dance | label | "Only When I Dance" |
| Only_When_I_Dance | altLabel | "Only When I Dance" |
| The_Wicked_Dreams_of_Paula_Schultz | type | Film |
| The_Wicked_Dreams_of_Paula_Schultz | type | NamedIndividual |
| The_Wicked_Dreams_of_Paula_Schultz | label | "The Wicked Dreams of Paula Schultz" |
| The_Wicked_Dreams_of_Paula_Schultz | altLabel | "The Wicked Dreams of Paula Schultz" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
