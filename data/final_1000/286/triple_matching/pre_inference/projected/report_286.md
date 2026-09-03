# Triple matching report: 286

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Vladimir_Vengerov | hasAwardReceived | People_s_Artist_of_the_RSFSR |
| Workers_Settlement | hasDirector | Vladimir_Vengerov |

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
| People_s_Artist_of_the_RSFSR | type | Award |
| People_s_Artist_of_the_RSFSR | type | NamedIndividual |
| People_s_Artist_of_the_RSFSR | label | "People's Artist of the RSFSR" |
| Vladimir_Vengerov | type | Person |
| Vladimir_Vengerov | type | NamedIndividual |
| Vladimir_Vengerov | label | "Vladimir Vengerov" |
| Vladimir_Vengerov | altLabel | "Vladimir Yakovlevich Vengerov" |
| Workers_Settlement | type | Film |
| Workers_Settlement | type | NamedIndividual |
| Workers_Settlement | label | "Workers' Settlement" |

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
