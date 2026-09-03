# Triple matching report: 164

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| American_Casino | hasDirector | Leslie_Cockburn |
| Leslie_Cockburn | hasAwardReceived | George_Polk_Award |

# 2. Unmatched triples

**Total unmatched count: 26**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 26**

| Subject | Predicate | Object |
|---|---|---|
| American_Casino | hasPublicationDate | "2009"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| American_Casino | type | Film |
| American_Casino | type | NamedIndividual |
| American_Casino | label | "American Casino" |
| George_Polk_Award | type | Award |
| George_Polk_Award | type | NamedIndividual |
| George_Polk_Award | label | "George Polk Award" |
| Leslie_Cockburn | hasAwardReceived | award_dupont |
| Leslie_Cockburn | hasAwardReceived | award_emmy |
| Leslie_Cockburn | hasAwardReceived | award_hillman_prize |
| Leslie_Cockburn | hasAwardReceived | award_rf_kennedy_journalism |
| Leslie_Cockburn | type | Person |
| Leslie_Cockburn | type | NamedIndividual |
| Leslie_Cockburn | label | "Leslie Cockburn" |
| award_dupont | type | Award |
| award_dupont | type | NamedIndividual |
| award_dupont | label | "Alfred I. duPont– Columbia University Award" |
| award_emmy | type | Award |
| award_emmy | type | NamedIndividual |
| award_emmy | label | "Emmy Award" |
| award_hillman_prize | type | Award |
| award_hillman_prize | type | NamedIndividual |
| award_hillman_prize | label | "The Hillman Prize" |
| award_rf_kennedy_journalism | type | Award |
| award_rf_kennedy_journalism | type | NamedIndividual |
| award_rf_kennedy_journalism | label | "Robert F. Kennedy Journalism Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 28 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 28 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 26 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.071429 |
| Recall | 1.000000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
