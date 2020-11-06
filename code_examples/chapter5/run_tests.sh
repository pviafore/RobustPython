#! /bin/bash -eu
python code_examples/chapter5/graph.py
python code_examples/chapter5/count_authors.py
python code_examples/chapter5/typeddict.py
python code_examples/chapter5/reverse.py
python code_examples/chapter5/generic.py
python code_examples/chapter5/overriding_dict.py
python code_examples/chapter5/userdict.py
python code_examples/chapter5/abc.py


mypy code_examples/chapter5/*.py


for f in code_examples/chapter5/invalid/*
do
	if mypy "$f" ; then
		echo "Expected $f to fail, but passed"
		exit 1;
	fi
done


echo "All Chapter 5 Tests Passed"
