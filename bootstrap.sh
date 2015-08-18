#!/usr/bin/env bash

# dotfiles
mkdir .dotfiles
cd .dotfiles
git clone https://github.com/sokolowskik/dotfiles.git .
chmod +x bootstrap.sh
./bootstrap.sh
