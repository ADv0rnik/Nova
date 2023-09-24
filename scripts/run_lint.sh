#!/bin/bash

BGreen='\033[1;32m'

# shellcheck disable=SC2034
cd ..
src_dir=$(pwd)

black "$src_dir"/adukar/courses


# shellcheck disable=SC1072
# shellcheck disable=SC1073
# shellcheck disable=SC1009
# shellcheck disable=SC1020
# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
  echo "Error running tests"
  exit 1
fi

black "$src_dir"/adukar/profiles

# shellcheck disable=SC1072
# shellcheck disable=SC1073
# shellcheck disable=SC1009
# shellcheck disable=SC1020
# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
  echo "Error running tests"
  exit 1
fi

echo -e "${BGreen}Checking complete!${BGreen}"