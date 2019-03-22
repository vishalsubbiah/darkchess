run:
	python run.py

test:
	pytest darkchess/tests/

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pytest_cache)" | xargs rm -rf
