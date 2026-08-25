# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
REQS = requirements.txt
TESTS = tests

# Default rule
all: run

# Rule to run the Python program
run: $(VENV)
	$(PYTHON) main.py

# Rule to create a virtual environment
$(VENV): $(REQS)
	python3 -m venv $(VENV)
	$(PIP) install -r $(REQS)

# Rule to install dependencies
install: $(VENV)

# Rule to run tests
# Rule to run tests
test: $(VENV)
	$(PYTHON) -m pytest $(TESTS)

# Phony targets
.PHONY: all run install test
