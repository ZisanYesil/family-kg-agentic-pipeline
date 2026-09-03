# Triple matching report: 410

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| I_Believe_in_Music | hasPerformer | Mac_Davis |
| Mac_Davis | hasBirthPlace | Lubbock_Texas |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| I_Believe_in_Music | type | CreativeWork |
| I_Believe_in_Music | type | NamedIndividual |
| I_Believe_in_Music | label | "I Believe in Music" |
| I_Believe_in_Music | altLabel | "I Believe in Music (song)" |
| Lubbock_Texas | type | Place |
| Lubbock_Texas | type | NamedIndividual |
| Lubbock_Texas | label | "Lubbock, Texas, United States" |
| Mac_Davis | type | Person |
| Mac_Davis | type | NamedIndividual |
| Mac_Davis | label | "Mac Davis" |
| Mac_Davis | altLabel | "Morris Mac Davis" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
