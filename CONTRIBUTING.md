# Contributing to Data Analyzer

Thank you for your interest in contributing! 🎉

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch** from `develop`
4. **Make your changes**
5. **Run tests and linters**
6. **Commit with conventional messages**
7. **Push and create a Pull Request**

## 📖 Development Workflow

### 1. Fork and Clone

```bash
# Fork the repo on GitHub, then clone your fork
git clone git@github.com:YOUR_USERNAME/data-analyzer.git
cd data-analyzer

# Add upstream remote
git remote add upstream git@github.com:intelingzhi/data-analyzer.git
```

### 2. Create a Feature Branch

```
# Sync with upstream
git fetch upstream
git checkout develop
git merge upstream/develop

# Create your feature branch
git checkout -b feature/your-feature-name
```

### 3. Make Changes
- Write clean, readable code
- Follow PEP 8 style guide
- Add docstrings to functions
- Write unit tests for new features

### 4. Run Quality Checks
```
# Format code
black src/ tests/

# Check style
flake8 src/ tests/

# Run tests
pytest

# Check coverage
pytest --cov=src --cov-report=html

```

### 5. Commit Your Changes
Follow Conventional Commits:
```
git commit -m "feat: add data normalization function"
git commit -m "fix: handle null values in cleaner"
git commit -m "docs: update README with new examples"

```

Commit types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- test: Tests
- refactor: Code refactoring
- style: Formatting
- chore: Maintenance


### 6. Push and Create PR
```
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub targeting the develop branch.

## 🧪 Testing Requirements
- All new code must have tests
- Minimum coverage: 95%
- Tests must pass on Python 3.9, 3.10, 3.11
## 📋 Code Review Process
1. At least 2 approvals required
2. All CI checks must pass
3. All comments must be resolved
4. Code must follow style guidelines

## ❓ Questions?
Open an issue or reach out to @intelingzhi.

