# Triple matching report: 32

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Adalberto_Pereira_dos_Santos | hasBirthDate | "1905-04-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Adalberto_Pereira_dos_Santos | hasDeathDate | "1984-04-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Louis_Armand_Constantin_de_Rohan | hasBirthDate | "1732-04-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Louis_Armand_Constantin_de_Rohan | hasDeathDate | "1794-07-27"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Adalberto_Pereira_dos_Santos | type | Person |
| Adalberto_Pereira_dos_Santos | type | NamedIndividual |
| Adalberto_Pereira_dos_Santos | label | "Adalberto Pereira dos Santos" |
| Adalberto_Pereira_dos_Santos | altLabel | "Adalberto Pereira dos Santos" |
| Louis_Armand_Constantin_de_Rohan | type | Person |
| Louis_Armand_Constantin_de_Rohan | type | NamedIndividual |
| Louis_Armand_Constantin_de_Rohan | label | "Louis-Armand-Constantin de Rohan" |
| Louis_Armand_Constantin_de_Rohan | altLabel | "Louis- Armand- Constantin de Rohan" |
| Louis_Armand_Constantin_de_Rohan | altLabel | "Louis‑Armand‑Constantin de Rohan" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 13 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.307692 |
| Recall | 1.000000 |
| F1 score | 0.470588 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
