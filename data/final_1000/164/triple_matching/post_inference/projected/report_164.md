# Triple matching report: 164

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| American_Casino | hasCreator | Leslie_Cockburn |
| American_Casino | hasDirector | Leslie_Cockburn |
| American_Casino | type | Artifact |
| American_Casino | type | CreativeWork |
| American_Casino | type | Film |
| George_Polk_Award | type | Award |
| Leslie_Cockburn | hasAwardReceived | George_Polk_Award |
| Leslie_Cockburn | type | Agent |
| Leslie_Cockburn | type | Person |

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
| American_Casino | hasPublicationDate | "2009"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Leslie_Cockburn | hasAwardReceived | award_dupont |
| Leslie_Cockburn | hasAwardReceived | award_emmy |
| Leslie_Cockburn | hasAwardReceived | award_hillman_prize |
| Leslie_Cockburn | hasAwardReceived | award_rf_kennedy_journalism |
| award_dupont | type | Award |
| award_emmy | type | Award |
| award_hillman_prize | type | Award |
| award_rf_kennedy_journalism | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 18 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.500000 |
| Recall | 1.000000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
