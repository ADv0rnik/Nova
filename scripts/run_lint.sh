#!/usr/bin/env bash


# shellcheck disable=SC2034
src_dir=$(dirname "$0")
echo "The name of the script is: $0"
echo "Source directory of the script: $src_dir"
#black .


# shellcheck disable=SC1072
# shellcheck disable=SC1073
# shellcheck disable=SC1009
# shellcheck disable=SC1020
if [ $? -ne 0 ]; then
  echo "Error running tests"
  exit 1
fi