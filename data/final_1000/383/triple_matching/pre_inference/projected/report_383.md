# Triple matching report: 383

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Juris_Podnieks | hasEducatedAt | VGIK |
| Vai_viegli_būt_jaunam | hasDirector | Juris_Podnieks |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Juris_Podnieks | type | Person |
| Juris_Podnieks | type | NamedIndividual |
| Juris_Podnieks | label | "Juris Podnieks" |
| VGIK | type | EducationalInstitution |
| VGIK | type | NamedIndividual |
| VGIK | label | "Soviet VGIK film school" |
| VGIK | altLabel | "VGIK film school" |
| Vai_viegli_būt_jaunam | type | Film |
| Vai_viegli_būt_jaunam | type | NamedIndividual |
| Vai_viegli_būt_jaunam | label | "Is It Easy To Be Young?" |
| Vai_viegli_būt_jaunam | altLabel | "Vai viegli būt jaunam?" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
