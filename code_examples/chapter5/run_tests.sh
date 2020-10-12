#! /bin/bash -eu
python code_examples/chapter4/fractions_example.py

mypy code_examples/chapter4/*.py

echo "All Chapter 4 Tests Passed"
