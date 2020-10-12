#! /bin/bash -eu
python code_examples/chapter3/mother_sauces_bad.py
python code_examples/chapter3/mother_sauces.py
python code_examples/chapter3/auto_enum.py
python code_examples/chapter3/auto_enum_generate.py
python code_examples/chapter3/allergen.py
python code_examples/chapter3/allergen_flag.py
python code_examples/chapter3/liquid_measure.py
python code_examples/chapter3/liquid_measure_intenum.py
python code_examples/chapter3/mother_sauces_alias.py
python code_examples/chapter3/mother_sauces_unique.py

mypy code_examples/chapter3/*.py

echo "All Chapter 3 Tests Passed"
