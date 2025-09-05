# ==============================================================================
# Makefile for Project Automation
#
# Provides a unified interface for common development tasks, such as running
# the application, formatting code, and running tests.
#
# Inspired by the self-documenting Makefile pattern.
# See: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# ==============================================================================

# Default target when 'make' is run without arguments
.DEFAULT_GOAL := help

# Specify the Python executable and main Streamlit file name
PYTHON := ./.venv/bin/python
STREAMLIT_APP_FILE := ./src/main.py

# ==============================================================================
# HELP
# ==============================================================================

.PHONY: help
help: ## Display this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%%-15s\033[0m %%s\n", $1, $2}' $(MAKEFILE_LIST)

# ==============================================================================
# ENVIRONMENT SETUP
# ==============================================================================

.PHONY: setup
setup: ## Project initial setup: install dependencies and create .env file
	@echo "🐍 Installing python dependencies with uv..."
	@uv sync


# ==============================================================================
# APPLICATION
# ==============================================================================

.PHONY: run
run: ## Simply execute src/main.py
	@echo "🚀 Executing src/main.py..."
	@$(PYTHON) $(STREAMLIT_APP_FILE)

# ==============================================================================
# CODE QUALITY
# ==============================================================================

.PHONY: format
format: ## Automatically format code using Black and Ruff
	@echo "🎨 Formatting code with black and ruff..."
	@black .
	@ruff check . --fix

.PHONY: lint
lint: ## Perform static code analysis (check) using Black and Ruff
	@echo "🔬 Linting code with black and ruff..."
	@black --check .
	@ruff check .

# ==============================================================================
# TESTING
# ==============================================================================

.PHONY: test
test: unit-test ## Run the full test suite

.PHONY: unit-test
unit-test: ## Run unit tests
	@echo "Running unit tests..."
	@PYTHONPATH=. $(PYTHON) -m pytest tests/unit -v -s
