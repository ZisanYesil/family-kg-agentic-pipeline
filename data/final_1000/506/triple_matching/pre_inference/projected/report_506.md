# Triple matching report: 506

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hans_Albrecht_Hereditary_Prince_of_Schleswig_Holstein | hasParent | Princess_Marie_Melita_of_Hohenlohe_Langenburg |
| Princess_Marie_Melita_of_Hohenlohe_Langenburg | hasParent | Ernst_II_Prince_of_Hohenlohe_Langenburg |

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
| Ernst_II_Prince_of_Hohenlohe_Langenburg | type | Person |
| Ernst_II_Prince_of_Hohenlohe_Langenburg | type | NamedIndividual |
| Ernst_II_Prince_of_Hohenlohe_Langenburg | label | "Ernst II, Prince of Hohenlohe-Langenburg" |
| Hans_Albrecht_Hereditary_Prince_of_Schleswig_Holstein | type | Person |
| Hans_Albrecht_Hereditary_Prince_of_Schleswig_Holstein | type | NamedIndividual |
| Hans_Albrecht_Hereditary_Prince_of_Schleswig_Holstein | label | "Hans Albrecht, Hereditary Prince of Schleswig-Holstein" |
| Hans_Albrecht_Hereditary_Prince_of_Schleswig_Holstein | altLabel | "Hans Albrecht, Hereditary Prince of Schleswig-Holstein-Sonderburg-Glücksburg" |
| Princess_Marie_Melita_of_Hohenlohe_Langenburg | type | Person |
| Princess_Marie_Melita_of_Hohenlohe_Langenburg | type | NamedIndividual |
| Princess_Marie_Melita_of_Hohenlohe_Langenburg | label | "Princess Marie Melita of Hohenlohe-Langenburg" |

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
