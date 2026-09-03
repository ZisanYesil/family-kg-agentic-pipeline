# Triple matching report: 297

# 1. Matched triples

**Count: 18**

| Subject | Predicate | Object |
|---|---|---|
| Boaz_Yakin | type | Agent |
| Chris_Briggs | type | Agent |
| Eli_Roth | type | Agent |
| Hostel_Part_II | hasProducer | Boaz_Yakin |
| Hostel_Part_II | hasProducer | Chris_Briggs |
| Hostel_Part_II | hasProducer | Eli_Roth |
| Hostel_Part_II | hasProducer | Mike_Fleiss |
| Hostel_Part_II | hasProducer | Quentin_Tarantino |
| Hostel_Part_II | hasProducer | Scott_Spiegel |
| Hostel_Part_II | type | Artifact |
| Hostel_Part_II | type | CreativeWork |
| Mike_Fleiss | type | Agent |
| Neruppu_Da | hasProducer | Vikram_Prabhu |
| Neruppu_Da | type | Artifact |
| Neruppu_Da | type | CreativeWork |
| Quentin_Tarantino | type | Agent |
| Scott_Spiegel | type | Agent |
| Vikram_Prabhu | type | Agent |

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
| Boaz_Yakin | type | Person |
| Chris_Briggs | type | Person |
| Eli_Roth | type | Person |
| Hostel_Part_II | type | Film |
| Mike_Fleiss | type | Person |
| Neruppu_Da | type | Film |
| Quentin_Tarantino | type | Person |
| Scott_Spiegel | type | Person |
| Vikram_Prabhu | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 9 |
| Extracted triples in scope | 27 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 27 |
| True positives (matched) | 18 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.666667 |
| Recall | 1.000000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
