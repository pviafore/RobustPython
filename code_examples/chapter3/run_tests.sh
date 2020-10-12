#! /bin/bash -eu
python code_examples/chapter3/find_workers.py
python code_examples/chapter3/variable_annotation.py
python code_examples/chapter3/invalid/invalid_example1.py
python code_examples/chapter3/invalid/invalid_example2.py
python code_examples/chapter3/invalid/invalid_example3.py
python code_examples/chapter3/invalid/invalid_type.py

mypy code_examples/chapter3/*.py

for f in code_examples/chapter3/invalid/* 
do
    ! mypy "$f" 2>/dev/null
done

echo "All Chapter 3 Tests Passed"
