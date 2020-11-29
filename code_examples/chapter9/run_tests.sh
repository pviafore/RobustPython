#! /bin/bash -eu
PYTHONPATH=. python code_examples/chapter9/fraction.py
PYTHONPATH=. python code_examples/chapter9/recipe.py
PYTHONPATH=. python code_examples/chapter9/nutritional_info.py
PYTHONPATH=. python code_examples/chapter9/frozen_recipe.py
PYTHONPATH=. python code_examples/chapter9/namedtuple.py

mypy code_examples/chapter9/*.py

echo "All Chapter 9 Tests Passed"
