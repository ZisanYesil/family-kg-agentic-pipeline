# Triple matching report: 901

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Geethapriya | hasDeathDate | "2016-01-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Red_Sundown | hasDirector | Jack_Arnold |
| Suvarna_Sethuve | hasDirector | Geethapriya |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Jack_Arnold_director | hasDeathDate | "1992-03-17"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Geethapriya | type | Person |
| Geethapriya | type | NamedIndividual |
| Geethapriya | label | "Geethapriya" |
| Geethapriya | altLabel | "Lakshman Rao Mohite" |
| Jack_Arnold | hasDeathDate | "1992-03-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jack_Arnold | type | Person |
| Jack_Arnold | type | NamedIndividual |
| Jack_Arnold | label | "Jack Arnold" |
| Red_Sundown | type | Film |
| Red_Sundown | type | NamedIndividual |
| Red_Sundown | label | "Red Sundown" |
| Suvarna_Sethuve | type | Film |
| Suvarna_Sethuve | type | NamedIndividual |
| Suvarna_Sethuve | label | "Suvarna Sethuve" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 18 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.176471 |
| Recall | 0.750000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
