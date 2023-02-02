setup:
	pip install -r requirements.txt

test:
	pytest .

run: test
	python main.py
