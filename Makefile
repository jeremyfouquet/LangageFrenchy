.ONESHELL:
.DEFAULT_GOAL:= run
P3 = python3
PYTHON= ./venv/bin/python3
PIP= ./venv/bin/pip3

venv/bin/activate: requirements.txt
	$(P3) -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
	$(PIP) install -r requirements.txt

venv: venv/bin/activate
	. ./venv/bin/activate

run: venv
	$(PYTHON) app/main.py

tests: venv
	$(PYTHON) app/test.py

clean:
	rm -rf app/__pycache__
	rm -rf venv

install-venv:
	sudo apt install $(P3) python3-venv

.PHONY: run clean tests install-venv