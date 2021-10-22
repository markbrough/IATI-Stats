#!/usr/bin/env bash

mkdir -p codelists/1
wget "https://iatistandard.org/reference_downloads/105/codelists/downloads/clv2/json/en/Version.json" -O codelists/1/Version.json
wget "https://iatistandard.org/reference_downloads/105/codelists/downloads/clv2/json/en/ActivityStatus.json" -O codelists/1/ActivityStatus.json
wget "https://iatistandard.org/reference_downloads/105/codelists/downloads/clv2/json/en/Currency.json" -O codelists/1/Currency.json
wget "https://iatistandard.org/reference_downloads/105/codelists/downloads/clv2/json/en/Sector.json" -O codelists/1/Sector.json
wget "https://iatistandard.org/reference_downloads/105/codelists/downloads/clv2/json/en/SectorCategory.json" -O codelists/1/SectorCategory.json
wget "https://iatistandard.org/reference_downloads/105/codelists/downloads/clv2/json/en/DocumentCategory.json" -O codelists/1/DocumentCategory.json
wget "https://iatistandard.org/reference_downloads/105/codelists/downloads/clv2/json/en/AidType.json" -O codelists/1/AidType.json
wget "https://iatistandard.org/reference_downloads/105/codelists/downloads/clv2/json/en/BudgetNotProvided.json" -O codelists/1/BudgetNotProvided.json

mkdir -p codelists/2
wget "https://codelists.codeforiati.org/api/json/en/Version.json" -O codelists/2/Version.json
wget "https://codelists.codeforiati.org/api/json/en/ActivityStatus.json" -O codelists/2/ActivityStatus.json
wget "https://codelists.codeforiati.org/api/json/en/Currency.json" -O codelists/2/Currency.json
wget "https://codelists.codeforiati.org/api/json/en/Sector.json" -O codelists/2/Sector.json
wget "https://codelists.codeforiati.org/api/json/en/SectorCategory.json" -O codelists/2/SectorCategory.json
wget "https://codelists.codeforiati.org/api/json/en/DocumentCategory.json" -O codelists/2/DocumentCategory.json
wget "https://codelists.codeforiati.org/api/json/en/AidType.json" -O codelists/2/AidType.json
wget "https://codelists.codeforiati.org/api/json/en/BudgetNotProvided.json" -O codelists/2/BudgetNotProvided.json
