.PHONY: help install install-dev run test lint format format-check audit clean ci

PYTHON ?= python
PIP ?= pip

help:
	@echo "Доступні команди:"
	@echo "make install - встановити залежності для запуску"
	@echo "make install-dev - встановити залежності для розробки"
	@echo "make run - запустити додаток"
	@echo "make test - виконати тести (unit + doctest)"
	@echo "make lint - перевірити стиль коду (flake8)"
	@echo "make format - відформатувати код (black)"
	@echo "make format-check - перевірити форматування без змін"
	@echo "make audit - перевірити вразливості у залежностях"
	@echo "make ci - повна перевірка (як у CI)"
	@echo "make clean - видалити проміжні файли"

install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements-dev.txt

run:
	$(PYTHON) src/word_counter.py

test:
	$(PYTHON) -m unittest discover -s tests -v

lint:
	$(PYTHON) -m flake8 src tests

format:
	$(PYTHON) -m black src tests

format-check:
	$(PYTHON) -m black --check src tests

audit:
	$(PYTHON) -m pip_audit -r requirements.txt

ci: format-check lint test audit

clean:
	rm -rf __pycache__ */__pycache__ */*/__pycache__
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov build dist *.egg-info
	find . -type f -name "*.pyc" -delete
