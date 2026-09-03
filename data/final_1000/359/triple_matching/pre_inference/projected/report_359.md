# Triple matching report: 359

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Marie_Frederike_of_Hesse_Kassel | hasParent | William_I_Elector_of_Hesse |
| William_I_Elector_of_Hesse | hasParent | Princess_Mary_of_Great_Britain |

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
| Marie_Frederike_of_Hesse_Kassel | type | Person |
| Marie_Frederike_of_Hesse_Kassel | type | NamedIndividual |
| Marie_Frederike_of_Hesse_Kassel | label | "Marie Frederike of Hesse-Kassel" |
| Marie_Frederike_of_Hesse_Kassel | altLabel | "Marie Friederike of Hesse-Kassel" |
| Princess_Mary_of_Great_Britain | type | Person |
| Princess_Mary_of_Great_Britain | type | NamedIndividual |
| Princess_Mary_of_Great_Britain | label | "Princess Mary of Great Britain" |
| William_I_Elector_of_Hesse | type | Person |
| William_I_Elector_of_Hesse | type | NamedIndividual |
| William_I_Elector_of_Hesse | label | "William I, Elector of Hesse" |

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
