#! /bin/bash -eu
PYTHONPATH=. python code_examples/chapter11/grocery_app.py

mypy code_examples/chapter11/*.py

echo "All Chapter 11 Tests Passed"
