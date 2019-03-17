test:
	pytest tests/
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pytest_cache)" | xargs rm -rf

run:
	python run.py