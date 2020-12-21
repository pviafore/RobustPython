#! /bin/bash -eu
python code_examples/chapter13/splittable.py
python code_examples/chapter13/splittable_inheritance.py
python code_examples/chapter13/iterator.py
python code_examples/chapter13/splittable_protocol.py
python code_examples/chapter13/runtime_checking.py
PYTHONPATH=code_examples/chapter13 python code_examples/chapter13/load_restaurant.py

mypy code_examples/chapter13/*.py

echo "All Chapter 13 Tests Passed"
