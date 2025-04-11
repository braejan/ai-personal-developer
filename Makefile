# Makefile for the AI Personal Developer project

.PHONY: test
test:
	pytest -v -ss --cov=src --cov-report=term-missing

.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".eggs" -exec rm -rf {} +

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make test       - Run tests with coverage report"
	@echo "  make clean      - Clean up Python cache and build files"
	@echo "  make help       - Show this help message"
