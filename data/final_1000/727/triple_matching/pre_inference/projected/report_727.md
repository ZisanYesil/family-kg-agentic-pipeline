# Triple matching report: 727

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Chantilly_Lace | hasDirector | Linda_Yellen |
| Linda_Yellen | hasAwardReceived | Emmys |

# 2. Unmatched triples

**Total unmatched count: 25**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 25**

| Subject | Predicate | Object |
|---|---|---|
| Chantilly_Lace | type | Film |
| Chantilly_Lace | type | NamedIndividual |
| Chantilly_Lace | label | "Chantilly Lace" |
| Emmys | type | Award |
| Emmys | type | NamedIndividual |
| Emmys | label | "Emmy Award" |
| Linda_Yellen | hasAwardReceived | christopher_award |
| Linda_Yellen | hasAwardReceived | peabody_award |
| Linda_Yellen | hasAwardReceived | primetime_emmy_award |
| Linda_Yellen | hasAwardReceived | silver_nymph_award |
| Linda_Yellen | type | Person |
| Linda_Yellen | type | NamedIndividual |
| Linda_Yellen | label | "Linda Yellen" |
| christopher_award | type | Award |
| christopher_award | type | NamedIndividual |
| christopher_award | label | "Christopher Award" |
| peabody_award | type | Award |
| peabody_award | type | NamedIndividual |
| peabody_award | label | "Peabody Award" |
| primetime_emmy_award | type | Award |
| primetime_emmy_award | type | NamedIndividual |
| primetime_emmy_award | label | "Primetime Emmy Award" |
| silver_nymph_award | type | Award |
| silver_nymph_award | type | NamedIndividual |
| silver_nymph_award | label | "Silver Nymph" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 27 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 27 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 25 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.074074 |
| Recall | 1.000000 |
| F1 score | 0.137931 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
