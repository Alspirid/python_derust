# Root orchestrator for the Python + TypeScript monorepo.
# Owns nothing language-specific — it fans out to each subdir's own tooling.
# Run `make` or `make help` to list targets.
.DEFAULT_GOAL := help

.PHONY: help install test-all lint-all fmt-all check-all clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Install both toolchains
	$(MAKE) -C python install
	pnpm -C typescript install

test-all: ## Run both test suites
	$(MAKE) -C python test
	pnpm -C typescript test

lint-all: ## Lint both languages
	$(MAKE) -C python lint
	pnpm -C typescript lint

fmt-all: ## Format both languages
	$(MAKE) -C python fmt
	pnpm -C typescript fmt

check-all: ## CI-style full check for both (lint + format + types + tests)
	$(MAKE) -C python check
	pnpm -C typescript check

clean: ## Clean caches/artifacts in both
	$(MAKE) -C python clean
	rm -rf typescript/node_modules typescript/coverage

# Passthroughs: `make py-<target>` -> python Makefile, `make ts-<script>` -> pnpm script.
# e.g. `make py-test-v`, `make ts-typecheck`, `make ts-fix`.
py-%: ## Run a target in python/ (e.g. make py-test)
	$(MAKE) -C python $*

ts-%: ## Run a pnpm script in typescript/ (e.g. make ts-test)
	pnpm -C typescript $*
