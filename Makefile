.PHONY: help install dev test lint format clean check-deps docs up down logs

# Default target
help:
	@echo "DevEx Sample - Developer Workflow"
	@echo "=================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies (for local development without Docker)
	pip install -r requirements.txt -r requirements-dev.txt

dev: ## Start service locally with Docker (docker compose up -d)
	docker compose up -d
	@echo "✓ Service started at http://localhost:5000"
	@echo "  View logs: make logs"
	@echo "  Stop: make down"

up: ## Alias for 'dev' - start services
	docker compose up -d

down: ## Stop services
	docker compose down
	@echo "✓ Services stopped"

logs: ## View service logs
	docker compose logs -f api

ps: ## Show running containers
	docker compose ps

test: ## Run unit tests with coverage
	pytest tests/ -v --cov=. --cov-report=html --cov-report=term-missing
	@echo "✓ Coverage report: htmlcov/index.html"

lint: ## Run code linters (black, flake8, isort)
	@echo "Running black..."
	black --check .
	@echo "Running flake8..."
	flake8 . --max-line-length=120 --exclude=.git,__pycache__,.venv,.pytest_cache,htmlcov
	@echo "Running isort..."
	isort --check-only .
	@echo "✓ All linters passed"

format: ## Auto-format code (black, isort)
	black .
	isort .
	@echo "✓ Code formatted"

check-deps: ## Check for outdated and vulnerable dependencies
	python scripts/check-deps.py

docs: ## Generate AI-based documentation (requires ANTHROPIC_API_KEY)
	python scripts/generate-docs.py

clean: ## Stop services, remove containers and volumes
	docker compose down -v
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name '.pytest_cache' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name 'htmlcov' -exec rm -rf {} + 2>/dev/null || true
	rm -f .coverage coverage.xml
	@echo "✓ Cleaned up"

# Advanced targets
build: ## Build Docker image
	docker compose build

rebuild: ## Rebuild Docker image (no cache)
	docker compose build --no-cache

shell: ## Open shell in running container
	docker compose exec api /bin/bash

run-app: ## Run app locally without Docker
	pip install -r requirements.txt
	python app.py

ci-check: test lint check-deps ## Run all CI checks locally
	@echo "✓ All CI checks passed!"

.DEFAULT_GOAL := help
