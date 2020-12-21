#! /bin/bash -eu
python code_examples/chapter12/restaurant.py
python code_examples/chapter12/square.py
python code_examples/chapter12/duck_type.py

mypy code_examples/chapter12/*.py

echo "All Chapter 12 Tests Passed"
