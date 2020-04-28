#!/usr/bin/env bash
set -x
pipenv install --dev
pipenv run invoke build.build-package
pipenv uninstall --all
pipenv run pip install homebrew-pypi-poet
pipenv run pip install washington_football -U
pipenv run poet -f washington_football > HomebrewFormula/washington_football.rb