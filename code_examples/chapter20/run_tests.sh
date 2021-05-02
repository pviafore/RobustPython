#! /bin/bash -eux
rm error.txt
PYTHONPATH=$(pwd)/code_examples/chapter20 pylint --load-plugins hotdog_checker code_examples/chapter20/hotdog.py > error.txt || true

grep "W0001: PreparedHotDog created outside of hotdog.prepare_for_serving. (unverified-prepared-hotdog)" error.txt 

echo "All Chapter 20 Tests Passed"
