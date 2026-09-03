# Triple matching report: 820

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Cornelis_Gijsbert_Gerrit_Jan_van_Steenis | hasBirthDate | "1901-10-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| Cornelis_Gijsbert_Gerrit_Jan_van_Steenis | hasDeathDate | "1986-05-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Tarsem_King_Baron_King_of_West_Bromwich | hasBirthDate | "1937-04-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Tarsem_King_Baron_King_of_West_Bromwich | hasDeathDate | "2013-01-09"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Cornelis_Gijsbert_Gerrit_Jan_van_Steenis | type | Person |
| Cornelis_Gijsbert_Gerrit_Jan_van_Steenis | type | NamedIndividual |
| Cornelis_Gijsbert_Gerrit_Jan_van_Steenis | label | "Cornelis Gijsbert Gerrit Jan van Steenis" |
| Cornelis_Gijsbert_Gerrit_Jan_van_Steenis | altLabel | "Cornelis Gijsbert Gerrit Jan Van Steenis" |
| Tarsem_King_Baron_King_of_West_Bromwich | type | Person |
| Tarsem_King_Baron_King_of_West_Bromwich | type | NamedIndividual |
| Tarsem_King_Baron_King_of_West_Bromwich | label | "Tarsem King, Baron King of West Bromwich" |
| Tarsem_King_Baron_King_of_West_Bromwich | altLabel | "Baron King of West Bromwich" |
| Tarsem_King_Baron_King_of_West_Bromwich | altLabel | "Tarsem King" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 13 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.307692 |
| Recall | 1.000000 |
| F1 score | 0.470588 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
