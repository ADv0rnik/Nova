#!/bin/bash

BGreen='\033[1;32m'
RED='\033[0;31m'
# shellcheck disable=SC2034
git_command="git rev-parse --git-dir"

# shellcheck disable=SC2154
# shellcheck disable=SC2034
GIT_DIR=$(eval "$git_command")

echo -e "${BGreen}Installing hooks...${BGreen}"

# Create symlink
ln -s ../../Nova/scripts/pre-commit.bash "$GIT_DIR"/hooks/pre-commit

# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
  echo -e "${RED}Failed to create symbolic link${RED}"
  exit 1
fi


echo -e "${BGreen}Installation complete!${BGreen}"