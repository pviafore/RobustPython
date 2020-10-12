#! /bin/bash -eu
python code_examples/chapter2/types_example.py
python code_examples/chapter2/memory_value.py
python code_examples/chapter2/double_items.py

# Just prints out - just grab errros
python code_examples/chapter2/print_items.py

mypy code_examples/chapter2/*.py

echo "All Chapter 2 Tests Passed"
