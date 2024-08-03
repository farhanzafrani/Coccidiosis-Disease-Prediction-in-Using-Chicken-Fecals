# Makefile for NTN_MLops environment

# Variables
VENV_NAME = NTN_MLops
PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip
ACTIVATE = . $(VENV_NAME)/bin/activate

# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  create-venv        Create a virtual environment"
	@echo "  install            Install all dependencies from requirements.txt"
	@echo "  freeze             Freeze the current dependencies to requirements.txt"
	@echo "  run-tests          Run tests with pytest"
	@echo "  format             Format code with black"
	@echo "  lint               Lint code with pylint"
	@echo "  clean              Remove Python file artifacts"
	@echo "  clean-venv         Remove the virtual environment"

# Create a virtual environment
create-venv:
	@python3 -m venv $(VENV_NAME)
	@echo "Virtual environment '$(VENV_NAME)' created."

# Install packages
install: $(VENV_NAME)
	@$(PIP) install -r requirements.txt
	@echo "Packages installed in the virtual environment."

# Freeze dependencies to requirements.txt
freeze: $(VENV_NAME)
	@$(PIP) freeze > requirements.txt
	@echo "Dependencies have been frozen to requirements.txt."

# Run tests
run-tests: $(VENV_NAME)
	@$(PYTHON) -m pytest
	@echo "Tests completed."

# Format code with black
format: $(VENV_NAME)
	@$(PYTHON) -m black .
	@echo "Code formatted with black."

# Lint the code with pylint
lint: $(VENV_NAME)
	@$(PYTHON) -m pylint .
	@echo "Linting completed with pylint."

# Clean Python file artifacts
clean:
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@echo "Cleaned Python file artifacts."

# Clean virtual environment
clean-venv:
	@rm -rf $(VENV_NAME)
	@echo "Virtual environment '$(VENV_NAME)' removed."

# Ensure virtual environment exists
$(VENV_NAME):
	@if [ ! -d "$(VENV_NAME)" ]; then $(MAKE) create-venv; fi
