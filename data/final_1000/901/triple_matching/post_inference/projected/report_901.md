# Triple matching report: 901

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Geethapriya | hasDeathDate | "2016-01-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Geethapriya | type | Agent |
| Geethapriya | type | Person |
| Jack_Arnold | type | Agent |
| Jack_Arnold | type | Person |
| Red_Sundown | hasCreator | Jack_Arnold |
| Red_Sundown | hasDirector | Jack_Arnold |
| Red_Sundown | type | Artifact |
| Red_Sundown | type | CreativeWork |
| Red_Sundown | type | Film |
| Suvarna_Sethuve | hasCreator | Geethapriya |
| Suvarna_Sethuve | hasDirector | Geethapriya |
| Suvarna_Sethuve | type | Artifact |
| Suvarna_Sethuve | type | CreativeWork |
| Suvarna_Sethuve | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Jack_Arnold_director | hasDeathDate | "1992-03-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jack_Arnold_director | type | Agent |
| Jack_Arnold_director | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Jack_Arnold | hasDeathDate | "1992-03-17"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 19 |
| True positives (matched) | 15 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.937500 |
| Recall | 0.833333 |
| F1 score | 0.882353 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
