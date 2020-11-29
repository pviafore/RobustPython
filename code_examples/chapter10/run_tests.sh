#! /bin/bash -eu
PYTHONPATH=. python code_examples/chapter10/person_construction.py
PYTHONPATH=. python code_examples/chapter10/pizza_maker.py
PYTHONPATH=. python code_examples/chapter10/pizza_maker_invariant.py
PYTHONPATH=. python code_examples/chapter10/pizza_maker_method.py

mypy code_examples/chapter10/*.py

echo "All Chapter 10 Tests Passed"
