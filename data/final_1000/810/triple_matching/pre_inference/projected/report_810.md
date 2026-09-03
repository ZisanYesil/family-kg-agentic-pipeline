# Triple matching report: 810

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Jacqueline_Lee_Kennedy_Onassis | hasBirthPlace | Southampton |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_Bouvier_Kennedy | hasParent | Jacqueline_Bouvier |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Caroline_Bouvier_Kennedy | hasParent | Jacqueline_Lee_Kennedy_Onassis |
| Caroline_Bouvier_Kennedy | type | Person |
| Caroline_Bouvier_Kennedy | type | NamedIndividual |
| Caroline_Bouvier_Kennedy | label | "Caroline Bouvier Kennedy" |
| Jacqueline_Lee_Kennedy_Onassis | type | Person |
| Jacqueline_Lee_Kennedy_Onassis | type | NamedIndividual |
| Jacqueline_Lee_Kennedy_Onassis | label | "Jacqueline Lee Kennedy Onassis" |
| Jacqueline_Lee_Kennedy_Onassis | altLabel | "Jacqueline Bouvier Kennedy" |
| Southampton | type | Place |
| Southampton | type | NamedIndividual |
| Southampton | label | "Southampton, New York" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
