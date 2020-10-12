#! /bin/bash -eu
python code_examples/chapter1/adjust_recipe.py
python code_examples/chapter1/adjust_recipe_wrong.py
python code_examples/chapter1/adjust_recipe_improved.py
python code_examples/chapter1/cookbooks.py
python code_examples/chapter1/cookbooks_counter.py
python code_examples/chapter1/cookbooks_defaultdict.py

python code_examples/chapter1/iteration.py 

# will fail 1 file until python 3.9 is released and mypy supports | operator
mypy code_examples/chapter1/*.py

echo "All Chapter 1 Tests Passed"
