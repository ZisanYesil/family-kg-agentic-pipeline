# Triple matching report: 22

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Ingegerd_Olofsdotter_of_Sweden | hasParent | Olof_Skötkonung |
| Olof_Skötkonung | hasParent | Sigrid_the_Haughty |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Ingegerd_Olofsdotter_of_Sweden | type | Person |
| Ingegerd_Olofsdotter_of_Sweden | type | NamedIndividual |
| Ingegerd_Olofsdotter_of_Sweden | label | "Ingegerd Olofsdotter of Sweden" |
| Ingegerd_Olofsdotter_of_Sweden | altLabel | "Anna" |
| Ingegerd_Olofsdotter_of_Sweden | altLabel | "Ingegerd Olofsdotter" |
| Ingegerd_Olofsdotter_of_Sweden | altLabel | "Ingegerd Olofsdotter of Sweden" |
| Ingegerd_Olofsdotter_of_Sweden | altLabel | "Irene" |
| Ingegerd_Olofsdotter_of_Sweden | altLabel | "Saint Anna" |
| Olof_Skötkonung | type | Person |
| Olof_Skötkonung | type | NamedIndividual |
| Olof_Skötkonung | label | "Olof Skötkonung" |
| Olof_Skötkonung | altLabel | "Olof Skötkonung" |
| Sigrid_the_Haughty | type | Person |
| Sigrid_the_Haughty | type | NamedIndividual |
| Sigrid_the_Haughty | label | "Sigrid the Haughty" |
| Sigrid_the_Haughty | altLabel | "Sigrid the Haughty" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 18 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.111111 |
| Recall | 1.000000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
