#! /bin/bash -eu
python code_examples/chapter17/call_repeat.py
python code_examples/chapter17/recommendation.py
python code_examples/chapter17/recommendation_improved.py

mypy code_examples/chapter17/*.py

echo "All Chapter 17 Tests Passed"
