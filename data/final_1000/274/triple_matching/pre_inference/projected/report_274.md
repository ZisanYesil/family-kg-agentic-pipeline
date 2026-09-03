# Triple matching report: 274

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_P_Jacobs | hasBirthDate | "1922-03-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Conquest_of_the_Planet_of_the_Apes | hasProducer | Arthur_P_Jacobs |
| I_m_Not_Harry_Jenson | hasProducer | Tom_Hern |
| Tom_Hern | hasBirthDate | "1984-12-10"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_P_Jacobs | type | Person |
| Arthur_P_Jacobs | type | NamedIndividual |
| Arthur_P_Jacobs | label | "Arthur P. Jacobs" |
| Conquest_of_the_Planet_of_the_Apes | type | Film |
| Conquest_of_the_Planet_of_the_Apes | type | NamedIndividual |
| Conquest_of_the_Planet_of_the_Apes | label | "Conquest of the Planet of the Apes" |
| I_m_Not_Harry_Jenson | type | Film |
| I_m_Not_Harry_Jenson | type | NamedIndividual |
| I_m_Not_Harry_Jenson | label | "I'm Not Harry Jenson" |
| Tom_Hern | type | Person |
| Tom_Hern | type | NamedIndividual |
| Tom_Hern | label | "Tom Hern" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
