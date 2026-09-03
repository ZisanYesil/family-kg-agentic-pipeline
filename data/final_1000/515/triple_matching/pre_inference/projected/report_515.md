# Triple matching report: 515

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Countess_Adelaide_of_Lippe_Biesterfeld | hasParent | Karoline_of_Wartensleben |
| Karoline_of_Wartensleben | hasBirthPlace | Mannheim |

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
| Countess_Adelaide_of_Lippe_Biesterfeld | type | Person |
| Countess_Adelaide_of_Lippe_Biesterfeld | type | NamedIndividual |
| Countess_Adelaide_of_Lippe_Biesterfeld | label | "Countess Adelaide of Lippe-Biesterfeld" |
| Karoline_of_Wartensleben | type | Person |
| Karoline_of_Wartensleben | type | NamedIndividual |
| Karoline_of_Wartensleben | label | "Countess Karoline Friederike Cäcilie Klothilde von Wartensleben" |
| Mannheim | type | Place |
| Mannheim | type | NamedIndividual |
| Mannheim | label | "Mannheim" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
