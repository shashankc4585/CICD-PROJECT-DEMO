install:
	python -m pip install -r requirements.txt

run:
	python src/ran_simulator.py

test:
	python -m pytest

clean:
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf tests/__pycache__