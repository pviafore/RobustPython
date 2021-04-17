#! /bin/bash -eu
python code_examples/chapter4/create_hot_dog.py
python code_examples/chapter4/create_hot_dog_defensive.py
python code_examples/chapter4/create_hot_dog_union.py
python code_examples/chapter4/product_type.py
python code_examples/chapter4/sum_type.py
python code_examples/chapter4/invalid/dispense_bun.py
python code_examples/chapter4/invalid/hotdog_invalid.py
python code_examples/chapter4/invalid/union_hotdog.py
python code_examples/chapter4/invalid/literals.py
python code_examples/chapter4/invalid/final.py
python code_examples/chapter4/invalid/newtype.py

mypy code_examples/chapter4/*.py

for f in code_examples/chapter4/invalid/* 
do
    ! mypy "$f" 2>/dev/null
done

echo "All Chapter 4 Tests Passed"
