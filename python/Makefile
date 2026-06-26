# Common project commands. Run `make` or `make help` to list them.
.DEFAULT_GOAL := help

.PHONY: help install test test-v lint fmt fmt-check fix typecheck check clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Sync dependencies (incl. the dev group)
	uv sync

test: ## Run the test suite
	uv run pytest

test-v: ## Run the test suite, verbose (one line per case)
	uv run pytest -v

lint: ## Lint with ruff
	uv run ruff check .

fmt: ## Auto-format with ruff
	uv run ruff format .

fmt-check: ## Check formatting without changing files
	uv run ruff format --check .

fix: ## Auto-fix lint issues with ruff
	uv run ruff check --fix .

typecheck: ## Type-check with pyright (via uvx — not a project dependency)
	uvx pyright src tests

check: lint fmt-check typecheck test ## Run lint + format check + type check + tests (CI-style)

clean: ## Remove Python/tool caches
	find . -path ./.venv -prune -o -name __pycache__ -type d -print -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache
