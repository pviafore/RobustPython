#! /bin/bash -eu
python code_examples/chapter15/restaurant_notification.py

mypy code_examples/chapter15/*.py

echo "All Chapter 15 Tests Passed"
