# Triple matching report: 274

# 1. Matched triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_P_Jacobs | hasBirthDate | "1922-03-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arthur_P_Jacobs | type | Agent |
| Arthur_P_Jacobs | type | Person |
| Conquest_of_the_Planet_of_the_Apes | hasProducer | Arthur_P_Jacobs |
| Conquest_of_the_Planet_of_the_Apes | type | Artifact |
| Conquest_of_the_Planet_of_the_Apes | type | CreativeWork |
| I_m_Not_Harry_Jenson | hasProducer | Tom_Hern |
| I_m_Not_Harry_Jenson | type | Artifact |
| I_m_Not_Harry_Jenson | type | CreativeWork |
| Tom_Hern | hasBirthDate | "1984-12-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| Tom_Hern | type | Agent |
| Tom_Hern | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Conquest_of_the_Planet_of_the_Apes | type | Film |
| I_m_Not_Harry_Jenson | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 12 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.857143 |
| Recall | 1.000000 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
