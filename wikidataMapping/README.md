# Wikidata Type Mapping

## About

Wikidata Type - DBpedia Type Mapping

## prerequisite
* `Python3`
* Wikidata Dump File[download here](https://dumps.wikimedia.org/wikidatawiki/entities/)

## How to use
refer `edu.kaist.mrlab.nn.pcnn.Main.java` and `PCNN.conf` files

### How to run
wikidata_dump.nt is file(https://dumps.wikimedia.org/wikidatawiki/entities/)
split -d -l {line number} wikidata_dump.nt wikidata_dumpPart_
cat wikidata_MappingTypePart_* > wikidata_MappingType.nt
`python3 classMapping.py`

## Maintainer
Yoosung Jung `wjd1004109@kaist.ac.kr`

## Publisher
[Machine Reading Lab](http://mrlab.kaist.ac.kr/) @ KAIST
