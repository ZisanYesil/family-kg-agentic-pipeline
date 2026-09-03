# Triple matching report: 160

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Guilty_2011_film | hasCountry | French |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Fanfare_of_Love | hasCountry | French |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Fanfare_of_Love | hasCountry | west_germany |
| Fanfare_of_Love | type | Film |
| Fanfare_of_Love | type | NamedIndividual |
| Fanfare_of_Love | label | "Fanfares of Love" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| Guilty_2011_film | type | Film |
| Guilty_2011_film | type | NamedIndividual |
| Guilty_2011_film | label | "Guilty" |
| west_germany | type | Country |
| west_germany | type | NamedIndividual |
| west_germany | label | "West Germany" |
| west_germany | altLabel | "West German" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.062500 |
| Recall | 0.500000 |
| F1 score | 0.111111 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
