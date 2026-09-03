# Triple matching report: 128

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Leicester_Devereux_6th_Viscount_Hereford | hasParent | Walter_Devereux_5th_Viscount_Hereford |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Walter_Devereux | hasCountry | English |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| English | type | Country |
| English | type | NamedIndividual |
| English | label | "England" |
| English | altLabel | "English" |
| Leicester_Devereux_6th_Viscount_Hereford | type | Person |
| Leicester_Devereux_6th_Viscount_Hereford | type | NamedIndividual |
| Leicester_Devereux_6th_Viscount_Hereford | label | "Leicester Devereux, 6th Viscount Hereford" |
| Walter_Devereux_5th_Viscount_Hereford | hasCountry | English |
| Walter_Devereux_5th_Viscount_Hereford | type | Person |
| Walter_Devereux_5th_Viscount_Hereford | type | NamedIndividual |
| Walter_Devereux_5th_Viscount_Hereford | label | "Walter Devereux, 5th Viscount Hereford" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
