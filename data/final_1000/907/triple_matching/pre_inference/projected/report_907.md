# Triple matching report: 907

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Friedrich_Gottlob_Uhlemann | hasEmployer | University_of_Berlin |
| Max_Uhlemann | hasParent | Friedrich_Gottlob_Uhlemann |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Friedrich_Gottlob_Uhlemann | hasEmployer | university_of_leipzig |
| Friedrich_Gottlob_Uhlemann | type | Person |
| Friedrich_Gottlob_Uhlemann | type | NamedIndividual |
| Friedrich_Gottlob_Uhlemann | label | "Friedrich Gottlob Uhlemann" |
| Max_Uhlemann | type | Person |
| Max_Uhlemann | type | NamedIndividual |
| Max_Uhlemann | label | "Max Uhlemann" |
| Max_Uhlemann | altLabel | "Maximilian Adolph Uhlemann" |
| University_of_Berlin | type | Organization |
| University_of_Berlin | type | NamedIndividual |
| University_of_Berlin | label | "University of Berlin" |
| university_of_leipzig | type | Organization |
| university_of_leipzig | type | NamedIndividual |
| university_of_leipzig | label | "University of Leipzig" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.125000 |
| Recall | 1.000000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
