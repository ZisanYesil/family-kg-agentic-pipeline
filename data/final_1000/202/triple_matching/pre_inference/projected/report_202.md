# Triple matching report: 202

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Mark_Mothersbaugh | hasEducatedAt | Kent_State_University |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Mama_s_Boy | hasComposer | Mark_Mothersbaugh |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Kent_State_University | type | EducationalInstitution |
| Kent_State_University | type | NamedIndividual |
| Kent_State_University | label | "Kent State University" |
| Kent_State_University | altLabel | "Kent State University" |
| Mama_s_Boy | type | Film |
| Mama_s_Boy | type | NamedIndividual |
| Mama_s_Boy | label | "Mama's Boy" |
| Mama_s_Boy | altLabel | "Mama's Boy" |
| Mark_Mothersbaugh | type | Person |
| Mark_Mothersbaugh | type | NamedIndividual |
| Mark_Mothersbaugh | label | "Mark Mothersbaugh" |
| Mark_Mothersbaugh | altLabel | "Mark Allen Mothersbaugh" |

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
