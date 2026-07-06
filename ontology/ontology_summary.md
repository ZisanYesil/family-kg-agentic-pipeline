# Ontology Summary

- Source: `ontology/family_orig.owl`
- Base IRI: `http://www.co-ode.org/roberts/family-tree.owl#`

## Classes

### Ancestor
- IRI: `http://www.example.com/genealogy.owl#Ancestor`
- Superclasses: Thing (`http://www.w3.org/2002/07/owl#Thing`)

### DomainEntity
- IRI: `http://www.example.com/genealogy.owl#DomainEntity`
- Superclasses: Thing (`http://www.w3.org/2002/07/owl#Thing`)

### Female
- IRI: `http://www.example.com/genealogy.owl#Female`
- Superclasses: Sex (`http://www.example.com/genealogy.owl#Sex`)

### Male
- IRI: `http://www.example.com/genealogy.owl#Male`
- Superclasses: Sex (`http://www.example.com/genealogy.owl#Sex`)

### Man
- IRI: `http://www.example.com/genealogy.owl#Man`
- Superclasses: Thing (`http://www.w3.org/2002/07/owl#Thing`)

### Marriage
- IRI: `http://www.example.com/genealogy.owl#Marriage`
- Superclasses: DomainEntity (`http://www.example.com/genealogy.owl#DomainEntity`)

### Person
- IRI: `http://www.example.com/genealogy.owl#Person`
- Superclasses: DomainEntity (`http://www.example.com/genealogy.owl#DomainEntity`)

### Sex
- IRI: `http://www.example.com/genealogy.owl#Sex`
- Superclasses: DomainEntity (`http://www.example.com/genealogy.owl#DomainEntity`)

### Woman
- IRI: `http://www.example.com/genealogy.owl#Woman`
- Superclasses: Thing (`http://www.w3.org/2002/07/owl#Thing`)

## Object Properties

### hasAncestor
- IRI: `http://www.example.com/genealogy.owl#hasAncestor`
- Domain: _None_
- Range: _None_
- Inverse property: isAncestorOf (`http://www.example.com/genealogy.owl#isAncestorOf`)
- Characteristics: transitive

### hasBrother
- IRI: `http://www.example.com/genealogy.owl#hasBrother`
- Domain: _None_
- Range: _None_
- Inverse property: isBrotherOf (`http://www.example.com/genealogy.owl#isBrotherOf`)
- Characteristics: _None_

### hasChild
- IRI: `http://www.example.com/genealogy.owl#hasChild`
- Domain: _None_
- Range: _None_
- Inverse property: isChildOf (`http://www.example.com/genealogy.owl#isChildOf`)
- Characteristics: _None_

### hasDaughter
- IRI: `http://www.example.com/genealogy.owl#hasDaughter`
- Domain: _None_
- Range: _None_
- Inverse property: isDaughterOf (`http://www.example.com/genealogy.owl#isDaughterOf`)
- Characteristics: _None_

### hasFather
- IRI: `http://www.example.com/genealogy.owl#hasFather`
- Domain: Person (`http://www.example.com/genealogy.owl#Person`)
- Range: Man (`http://www.example.com/genealogy.owl#Man`)
- Inverse property: isFatherOf (`http://www.example.com/genealogy.owl#isFatherOf`)
- Characteristics: functional

### hasFemalePartner
- IRI: `http://www.example.com/genealogy.owl#hasFemalePartner`
- Domain: Marriage (`http://www.example.com/genealogy.owl#Marriage`)
- Range: Woman (`http://www.example.com/genealogy.owl#Woman`)
- Inverse property: isFemalePartnerIn (`http://www.example.com/genealogy.owl#isFemalePartnerIn`)
- Characteristics: _None_

### hasHusband
- IRI: `http://www.example.com/genealogy.owl#hasHusband`
- Domain: _None_
- Range: Man (`http://www.example.com/genealogy.owl#Man`)
- Inverse property: isHusbandOf (`http://www.example.com/genealogy.owl#isHusbandOf`)
- Characteristics: _None_

### hasMalePartner
- IRI: `http://www.example.com/genealogy.owl#hasMalePartner`
- Domain: Marriage (`http://www.example.com/genealogy.owl#Marriage`)
- Range: Man (`http://www.example.com/genealogy.owl#Man`)
- Inverse property: isMalePartnerIn (`http://www.example.com/genealogy.owl#isMalePartnerIn`)
- Characteristics: _None_

### hasMother
- IRI: `http://www.example.com/genealogy.owl#hasMother`
- Domain: Person (`http://www.example.com/genealogy.owl#Person`)
- Range: Woman (`http://www.example.com/genealogy.owl#Woman`)
- Inverse property: isMotherOf (`http://www.example.com/genealogy.owl#isMotherOf`)
- Characteristics: functional

### hasParent
- IRI: `http://www.example.com/genealogy.owl#hasParent`
- Domain: Person (`http://www.example.com/genealogy.owl#Person`)
- Range: Person (`http://www.example.com/genealogy.owl#Person`)
- Inverse property: isParentOf (`http://www.example.com/genealogy.owl#isParentOf`)
- Characteristics: _None_

### hasPartner
- IRI: `http://www.example.com/genealogy.owl#hasPartner`
- Domain: Marriage (`http://www.example.com/genealogy.owl#Marriage`)
- Range: Person (`http://www.example.com/genealogy.owl#Person`)
- Inverse property: isPartnerIn (`http://www.example.com/genealogy.owl#isPartnerIn`)
- Characteristics: _None_

### hasRelation
- IRI: `http://www.example.com/genealogy.owl#hasRelation`
- Domain: Person (`http://www.example.com/genealogy.owl#Person`)
- Range: Person (`http://www.example.com/genealogy.owl#Person`)
- Inverse property: hasRelation (`http://www.example.com/genealogy.owl#hasRelation`)
- Characteristics: symmetric

### hasSex
- IRI: `http://www.example.com/genealogy.owl#hasSex`
- Domain: Person (`http://www.example.com/genealogy.owl#Person`)
- Range: Sex (`http://www.example.com/genealogy.owl#Sex`)
- Inverse property: _None_
- Characteristics: functional

### hasSister
- IRI: `http://www.example.com/genealogy.owl#hasSister`
- Domain: _None_
- Range: _None_
- Inverse property: isSisterOf (`http://www.example.com/genealogy.owl#isSisterOf`)
- Characteristics: _None_

### hasSon
- IRI: `http://www.example.com/genealogy.owl#hasSon`
- Domain: _None_
- Range: _None_
- Inverse property: isSonOf (`http://www.example.com/genealogy.owl#isSonOf`)
- Characteristics: _None_

### hasSpouse
- IRI: `http://www.example.com/genealogy.owl#hasSpouse`
- Domain: _None_
- Range: _None_
- Inverse property: isSpouseOf (`http://www.example.com/genealogy.owl#isSpouseOf`)
- Characteristics: _None_

### hasWife
- IRI: `http://www.example.com/genealogy.owl#hasWife`
- Domain: _None_
- Range: Woman (`http://www.example.com/genealogy.owl#Woman`)
- Inverse property: isWifeOf (`http://www.example.com/genealogy.owl#isWifeOf`)
- Characteristics: _None_

### isAncestorOf
- IRI: `http://www.example.com/genealogy.owl#isAncestorOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasAncestor (`http://www.example.com/genealogy.owl#hasAncestor`)
- Characteristics: _None_

### isBloodrelationOf
- IRI: `http://www.example.com/genealogy.owl#isBloodrelationOf`
- Domain: _None_
- Range: _None_
- Inverse property: _None_
- Characteristics: _None_

### isBrotherOf
- IRI: `http://www.example.com/genealogy.owl#isBrotherOf`
- Domain: Man (`http://www.example.com/genealogy.owl#Man`)
- Range: Person (`http://www.example.com/genealogy.owl#Person`)
- Inverse property: hasBrother (`http://www.example.com/genealogy.owl#hasBrother`)
- Characteristics: _None_

### isChildOf
- IRI: `http://www.example.com/genealogy.owl#isChildOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasChild (`http://www.example.com/genealogy.owl#hasChild`)
- Characteristics: _None_

### isDaughterOf
- IRI: `http://www.example.com/genealogy.owl#isDaughterOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasDaughter (`http://www.example.com/genealogy.owl#hasDaughter`)
- Characteristics: _None_

### isFatherOf
- IRI: `http://www.example.com/genealogy.owl#isFatherOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasFather (`http://www.example.com/genealogy.owl#hasFather`)
- Characteristics: _None_

### isFemalePartnerIn
- IRI: `http://www.example.com/genealogy.owl#isFemalePartnerIn`
- Domain: _None_
- Range: _None_
- Inverse property: hasFemalePartner (`http://www.example.com/genealogy.owl#hasFemalePartner`)
- Characteristics: _None_

### isHusbandOf
- IRI: `http://www.example.com/genealogy.owl#isHusbandOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasHusband (`http://www.example.com/genealogy.owl#hasHusband`)
- Characteristics: _None_

### isMalePartnerIn
- IRI: `http://www.example.com/genealogy.owl#isMalePartnerIn`
- Domain: _None_
- Range: _None_
- Inverse property: hasMalePartner (`http://www.example.com/genealogy.owl#hasMalePartner`)
- Characteristics: _None_

### isMotherOf
- IRI: `http://www.example.com/genealogy.owl#isMotherOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasMother (`http://www.example.com/genealogy.owl#hasMother`)
- Characteristics: _None_

### isParentOf
- IRI: `http://www.example.com/genealogy.owl#isParentOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasParent (`http://www.example.com/genealogy.owl#hasParent`)
- Characteristics: _None_

### isPartnerIn
- IRI: `http://www.example.com/genealogy.owl#isPartnerIn`
- Domain: _None_
- Range: _None_
- Inverse property: hasPartner (`http://www.example.com/genealogy.owl#hasPartner`)
- Characteristics: _None_

### isSiblingOf
- IRI: `http://www.example.com/genealogy.owl#isSiblingOf`
- Domain: _None_
- Range: _None_
- Inverse property: isSiblingOf (`http://www.example.com/genealogy.owl#isSiblingOf`)
- Characteristics: symmetric, transitive

### isSisterOf
- IRI: `http://www.example.com/genealogy.owl#isSisterOf`
- Domain: Woman (`http://www.example.com/genealogy.owl#Woman`)
- Range: Person (`http://www.example.com/genealogy.owl#Person`)
- Inverse property: hasSister (`http://www.example.com/genealogy.owl#hasSister`)
- Characteristics: _None_

### isSonOf
- IRI: `http://www.example.com/genealogy.owl#isSonOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasSon (`http://www.example.com/genealogy.owl#hasSon`)
- Characteristics: _None_

### isSpouseOf
- IRI: `http://www.example.com/genealogy.owl#isSpouseOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasSpouse (`http://www.example.com/genealogy.owl#hasSpouse`)
- Characteristics: _None_

### isUncleOf
- IRI: `http://www.example.com/genealogy.owl#isUncleOf`
- Domain: Man (`http://www.example.com/genealogy.owl#Man`)
- Range: Person (`http://www.example.com/genealogy.owl#Person`)
- Inverse property: _None_
- Characteristics: _None_

### isWifeOf
- IRI: `http://www.example.com/genealogy.owl#isWifeOf`
- Domain: _None_
- Range: _None_
- Inverse property: hasWife (`http://www.example.com/genealogy.owl#hasWife`)
- Characteristics: _None_

## Data Properties

_No data properties declared._

## Restrictions

### Ancestor
- Class IRI: `http://www.example.com/genealogy.owl#Ancestor`
- Source: `equivalent_to`; property=isAncestorOf (`http://www.example.com/genealogy.owl#isAncestorOf`); type=someValuesFrom; value=Person (`http://www.example.com/genealogy.owl#Person`)

### Man
- Class IRI: `http://www.example.com/genealogy.owl#Man`
- Source: `equivalent_to`; property=hasSex (`http://www.example.com/genealogy.owl#hasSex`); type=someValuesFrom; value=Male (`http://www.example.com/genealogy.owl#Male`)

### Person
- Class IRI: `http://www.example.com/genealogy.owl#Person`
- Source: `is_a`; property=hasFather (`http://www.example.com/genealogy.owl#hasFather`); type=someValuesFrom; value=Man (`http://www.example.com/genealogy.owl#Man`)
- Source: `is_a`; property=hasMother (`http://www.example.com/genealogy.owl#hasMother`); type=someValuesFrom; value=Woman (`http://www.example.com/genealogy.owl#Woman`)
- Source: `is_a`; property=hasSex (`http://www.example.com/genealogy.owl#hasSex`); type=someValuesFrom; value=Sex (`http://www.example.com/genealogy.owl#Sex`)
- Source: `is_a`; property=hasParent (`http://www.example.com/genealogy.owl#hasParent`); type=maxCardinality; value=Person (`http://www.example.com/genealogy.owl#Person`); cardinality=2

### Woman
- Class IRI: `http://www.example.com/genealogy.owl#Woman`
- Source: `equivalent_to`; property=hasSex (`http://www.example.com/genealogy.owl#hasSex`); type=someValuesFrom; value=Female (`http://www.example.com/genealogy.owl#Female`)

## Disjoint Classes

- Female (`http://www.example.com/genealogy.owl#Female`), Male (`http://www.example.com/genealogy.owl#Male`)
- Person (`http://www.example.com/genealogy.owl#Person`), Sex (`http://www.example.com/genealogy.owl#Sex`)