#! /bin/bash -eu
PYTHONPATH=. python code_examples/chapter7/main.py


mypy code_examples/chapter7/*.py
monkeytype run code_examples/chapter7/main.py


echo "All Chapter 7 Tests Passed"
