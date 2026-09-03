# Triple matching report: 920

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Gordon_Douglas | type | Agent |
| Gordon_Douglas | type | Person |
| Gunther_von_Fritsch | hasBirthDate | "1906-07-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gunther_von_Fritsch | type | Agent |
| Gunther_von_Fritsch | type | Person |
| Stolen_Identity | hasCreator | Gunther_von_Fritsch |
| Stolen_Identity | hasDirector | Gunther_von_Fritsch |
| Stolen_Identity | type | Artifact |
| Stolen_Identity | type | CreativeWork |
| Stolen_Identity | type | Film |
| Them | hasCreator | Gordon_Douglas |
| Them | hasDirector | Gordon_Douglas |
| Them | type | Artifact |
| Them | type | CreativeWork |
| Them | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Gordon_Douglas_director | hasBirthDate | "1907-12-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gordon_Douglas_director | type | Agent |
| Gordon_Douglas_director | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Gordon_Douglas | hasBirthDate | "1907-12-15"^^<http://www.w3.org/2001/XMLSchema#date> |

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
