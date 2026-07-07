UV ?= uv

.PHONY: sync
sync:
	$(UV) sync --all-groups

.PHONY: lock
lock:
	$(UV) lock

.PHONY: generate
gen generate:
	$(UV) run python generate.py

.PHONY: build
build: generate
	$(UV) run mkdocs build

.PHONY: serve
serve: generate
	$(UV) run mkdocs serve --livereload -o --dev-addr 127.0.0.1:6969

.PHONY: lint
lint:
	$(UV) run ruff check .

.PHONY: format
format:
	$(UV) run ruff format .

.PHONY: typecheck
typecheck:
	$(UV) run mypy .

.PHONY: clean
clean:
	rm -rf .venv site
	find . -name '__pycache__' -type d -exec rm -rf {} +
	find . -name '*.pyc' -delete

.PHONY: all
all: lint typecheck build
