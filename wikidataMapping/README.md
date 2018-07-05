# Wikidata Type Mapping

## About

Wikidata Type - DBpedia Type Mapping

## prerequisite
* `Python3`
* Wikidata Dump File [download here](https://dumps.wikimedia.org/wikidatawiki/entities/)

## How to use
wikidata_dump.nt is file(https://dumps.wikimedia.org/wikidatawiki/entities/)
<br>
split -d -l {line number} wikidata_dump.nt wikidata_dumpPart_
<br>
cat wikidata_MappingTypePart_* > wikidata_MappingType.nt
<br><br>
equivalentClass is DBpedia Ontology Type equivalentClass wikidata entity type
<br><br>
sameAsWikidata.nt is DBpedia entity sameAs wikidata entity

### How to run
`python3 classMapping.py`

## Maintainer
Yoosung Jung `wjd1004109@kaist.ac.kr`

## Publisher
[Machine Reading Lab](http://mrlab.kaist.ac.kr/) @ KAIST

