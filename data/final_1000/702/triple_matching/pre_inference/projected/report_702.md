# Triple matching report: 702

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Charlotte_of_Hesse_Kassel | hasSpouse | Charles_I_Louis_Elector_Palatine |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Charles_I_Louis_Elector_Palatine | hasParent | Frederick_V |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Charles_I_Louis_Elector_Palatine | type | Person |
| Charles_I_Louis_Elector_Palatine | type | NamedIndividual |
| Charles_I_Louis_Elector_Palatine | label | "Charles I Louis, Elector Palatine" |
| Charles_I_Louis_Elector_Palatine | altLabel | "Charles Louis, Elector Palatine" |
| Charlotte_of_Hesse_Kassel | type | Person |
| Charlotte_of_Hesse_Kassel | type | NamedIndividual |
| Charlotte_of_Hesse_Kassel | label | "Charlotte of Hesse-Kassel" |
| Charlotte_of_Hesse_Kassel | altLabel | "Landgravine Charlotte of Hesse-Kassel" |
| Frederick_V | hasChild | Charles_I_Louis_Elector_Palatine |
| Frederick_V | type | Person |
| Frederick_V | type | NamedIndividual |
| Frederick_V | label | "Frederick V of the Palatinate" |

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
