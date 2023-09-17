#!/usr/bin/env bash


black .
python lint.py -p ../Nova/adukar/

# shellcheck disable=SC1072
# shellcheck disable=SC1073
# shellcheck disable=SC1009
# shellcheck disable=SC1020
if [ $? -ne 0]; then
  echo "Error running tests"
  exit 1
fi