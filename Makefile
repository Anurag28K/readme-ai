# Makefile

SHELL := /bin/bash
VENV := readmeai

.PHONY: help clean format lint conda-recipe git-rm-cache file-search test poetry-reqs

help:
	@echo "Commands:"
	@echo "clean        : repository file cleanup."
	@echo "format       : executes code formatting."
	@echo "lint         : executes code linting."
	@echo "conda-recipe  : builds conda package."
	@echo "git-rm-cache : fix git untracked files."
	@echo "file-search  : search for text in files."
	@echo "test         : executes tests."
	@echo "poetry-reqs  : generates requirements.txt file."

.PHONY: clean
clean:
	./scripts/clean.sh clean

.PHONY: format
format:
	@echo -e "\nFormatting in directory: ${CURDIR}"
	black ${CURDIR}
	isort ${CURDIR}

.PHONY: lint
lint:
	@echo -e "\nLinting in directory: ${CURDIR}"
	flake8 ${CURDIR}
	ruff ${CURDIR}

.PHONY: conda-recipe
conda-recipe:
	grayskull pypi readmeai
	conda build .

.PHONY: git-rm-cache
git-rm-cache:
	git rm -r --cached .

.PHONY: file-search
file-search:
	grep -R "ENTRYPOINT" .

.PHONY: test
test:
	pytest \
	-n auto \
	--cov=./ \
	--cov-report=xml \
	--cov-report=term-missing \
	--cov-branch

.PHONY: poetry-reqs
poetry-reqs:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
