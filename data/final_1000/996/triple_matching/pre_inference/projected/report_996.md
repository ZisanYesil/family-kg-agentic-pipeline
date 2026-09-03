# Triple matching report: 996

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| There_s_No_Tomorrow | hasDirector | Max_Ophüls |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | hasBirthPlace | Saarbrücken |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | hasBirthPlace | country_germany |
| Max_Ophüls | type | Person |
| Max_Ophüls | type | NamedIndividual |
| Max_Ophüls | label | "Max Ophüls" |
| Max_Ophüls | altLabel | "Maximillian Oppenheimer" |
| There_s_No_Tomorrow | type | Film |
| There_s_No_Tomorrow | type | NamedIndividual |
| There_s_No_Tomorrow | label | "There's No Tomorrow" |
| country_germany | type | Country |
| country_germany | type | NamedIndividual |
| country_germany | label | "Germany" |
| country_germany | altLabel | "German" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
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
