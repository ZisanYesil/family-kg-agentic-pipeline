# Triple matching report: 969

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Phil_Rosen | hasBirthDate | "1888-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Phil_Rosen | type | Agent |
| Phil_Rosen | type | Person |
| Texas_Gun_Fighter | hasCreator | Phil_Rosen |
| Texas_Gun_Fighter | hasDirector | Phil_Rosen |
| Texas_Gun_Fighter | type | Artifact |
| Texas_Gun_Fighter | type | CreativeWork |
| Texas_Gun_Fighter | type | Film |
| What_Will_People_Say | type | Artifact |
| What_Will_People_Say | type | CreativeWork |
| What_Will_People_Say | type | Film |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Alice_Guy | type | Agent |
| Alice_Guy | type | Person |
| Alice_Guy_Blaché | hasBirthDate | "1873-07-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Alice_Guy_Blaché | type | Agent |
| Alice_Guy_Blaché | type | Person |
| What_Will_People_Say | hasCreator | Alice_Guy |
| What_Will_People_Say | hasDirector | Alice_Guy |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| What_Will_People_Say | hasCreator | alice_guy |
| What_Will_People_Say | hasDirector | alice_guy |
| alice_guy | hasBirthDate | "1873-07-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| alice_guy | type | Agent |
| alice_guy | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 23 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 7 |
| Precision | 0.687500 |
| Recall | 0.611111 |
| F1 score | 0.647059 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
