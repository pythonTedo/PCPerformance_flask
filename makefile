TEST_HOST ?= localhost:5000

SRC_DIR := src

.DEFAULT_GOAL := help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

test: ## Run tests
	echo "Running tests"
	. $(SRC_DIR)/venv/bin/activate && pytest -v
	
test-report: ## Run tests and generate report
	. ../venv/bin/activate && pytest --junitxml=report.xml

run: ## Run the app
	. ../venv/bin/activate && python $(SRC_DIR)/run.py


#==============================================================================