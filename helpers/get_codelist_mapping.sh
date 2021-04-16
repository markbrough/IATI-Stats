#!/usr/bin/env bash

wget https://raw.github.com/IATI/IATI-Codelists/version-1.05/mapping.xml -O mapping-1.xml
python mappings_to_json.py mapping-1.xml > mapping-1.json

wget https://raw.github.com/IATI/IATI-Codelists/version-2.03/mapping.xml -O mapping-2.xml
wget https://raw.github.com/codeforIATI/Unofficial-Codelists/master/mapping.xml -O mapping-unofficial.xml
python mappings_to_json.py mapping-2.xml mapping-unofficial.xml > mapping-2.json
