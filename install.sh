#/usr/bin/env bash

# choice shell
if [ "$SHELL" == "/bin/bash" ]
then
  CONFIG_FILE="$HOME/.bashrc"
elif [ "$SHELL" == "/bin/zsh" ]
then
  CONFIG_FILE="$HOME/.zshrc"
else
  echo "NOT SUPPORT THIS SHELL: $SHELL"
  exit 1
fi

EXEC_PY_FILE="$(pwd)/server_tag.py"

# write config
echo "write config"
{
  echo "#server_tag alias config"
  echo "alias _ssh=\"/usr/bin/ssh\""
  echo "alias ssh=\"$EXEC_PY_FILE\""
} >> "$CONFIG_FILE"
echo "write done"

echo "generate config to $(pwd)/server_config.json"
python3 "$(pwd)/generate_config.py"
echo "generate done"

# finish
echo "install SUCCESS, reopen your iterm2."