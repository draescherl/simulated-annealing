env:
	source ./venv/bin/activate

install:
	pip install -r requirements.txt

.PHONY: env install