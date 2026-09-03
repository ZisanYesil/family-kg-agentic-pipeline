# Triple matching report: 700

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Alfred_Vohrer | hasCountry | German |
| Long_Legs_Long_Fingers | hasDirector | Alfred_Vohrer |
| Olaf_Ittenbach | hasCountry | German |
| Premutos_The_Fallen_Angel | hasDirector | Olaf_Ittenbach |

# 2. Unmatched triples

**Total unmatched count: 21**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 21**

| Subject | Predicate | Object |
|---|---|---|
| Alfred_Vohrer | type | Person |
| Alfred_Vohrer | type | NamedIndividual |
| Alfred_Vohrer | label | "Alfred Vohrer" |
| Alfred_Vohrer | altLabel | "Alfred Vohrer" |
| German | type | Country |
| German | type | NamedIndividual |
| German | label | "Germany" |
| German | altLabel | "German" |
| German | altLabel | "Germany" |
| Long_Legs_Long_Fingers | type | Film |
| Long_Legs_Long_Fingers | type | NamedIndividual |
| Long_Legs_Long_Fingers | label | "Long Legs, Long Fingers" |
| Long_Legs_Long_Fingers | altLabel | "Long Legs, Long Fingers" |
| Olaf_Ittenbach | type | Person |
| Olaf_Ittenbach | type | NamedIndividual |
| Olaf_Ittenbach | label | "Olaf Ittenbach" |
| Olaf_Ittenbach | altLabel | "Olaf Ittenbach" |
| Premutos_The_Fallen_Angel | type | Film |
| Premutos_The_Fallen_Angel | type | NamedIndividual |
| Premutos_The_Fallen_Angel | label | "Premutos: The Fallen Angel" |
| Premutos_The_Fallen_Angel | altLabel | "Premutos: The Fallen Angel" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 25 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 25 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 21 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.160000 |
| Recall | 1.000000 |
| F1 score | 0.275862 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
