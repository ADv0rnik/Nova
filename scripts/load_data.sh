#!/bin/bash

RED='\033[0;31m'
BGreen='\033[1;32m'

echo -e "${BGreen}Running data load...${BGreen}"
cd ..

set -o allexport
source .env set
set +o allexport

# shellcheck disable=SC1073
# shellcheck disable=SC1009

if [[ $LOAD_FIXTURES == True ]]; then
  python manage.py loaddata db.json
  # shellcheck disable=SC2181
  if [ $? -ne 0 ]; then
    echo -e "${RED}Error loading data...${RED}"
    exit 1
  fi
  echo -e ${BGreen}"Fixtures have been installed"${BGreen}
fi