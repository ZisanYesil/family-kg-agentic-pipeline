# Triple matching report: 966

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Louis_IX_Landgrave_of_Hesse_Darmstadt | hasDeathPlace | Pirmasens |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_of_Hesse_Darmstadt | hasParent | Louis_IX_Landgrave_of_Hesse_Darmstadt |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_of_Hesse_Darmstadt | type | Person |
| Caroline_of_Hesse_Darmstadt | type | NamedIndividual |
| Caroline_of_Hesse_Darmstadt | label | "Caroline of Hesse-Darmstadt" |
| Caroline_of_Hesse_Darmstadt | altLabel | "Princess Caroline of Hesse-Darmstadt" |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | hasParent | Caroline_of_Hesse_Darmstadt |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | type | Person |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | type | NamedIndividual |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | label | "Louis IX, Landgrave of Hesse-Darmstadt" |
| Louis_IX_Landgrave_of_Hesse_Darmstadt | altLabel | "Louis IX" |
| Pirmasens | type | Place |
| Pirmasens | type | NamedIndividual |
| Pirmasens | label | "Pirmasens" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
