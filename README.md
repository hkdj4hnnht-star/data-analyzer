# Data Analyzer

[![CI](https://github.com/intelingzhi/data-analyzer/workflows/CI/badge.svg)](https://github.com/intelingzhi/data-analyzer/actions)
[![codecov](https://codecov.io/gh/intelingzhi/data-analyzer/branch/main/graph/badge.svg)](https://codecov.io/gh/intelingzhi/data-analyzer)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-grade Python library for data cleaning and exploratory analysis.

## ✨ Features

- **Data Cleaning**: Remove duplicates, handle missing values, normalize data types
- **Statistical Analysis**: Descriptive statistics, correlation analysis
- **Data Validation**: Schema validation, constraint checking
- **Export Support**: CSV, JSON, Parquet formats

## 🚀 Installation

```bash
pip install data-analyzer
```
## 📖 Quick Start
```
from data_analyzer import DataCleaner

# Initialize cleaner
cleaner = DataCleaner()

# Load and clean data
data = cleaner.load_csv('data.csv')
cleaned_data = cleaner.remove_duplicates(data)
```
## 🧪 Development Setup
```
# Clone the repository
git clone https://github.com/intelingzhi/data-analyzer.git
cd data-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linters
flake8 src/ tests/
black --check src/ tests/
```
## 🤝 Contributing
We welcome contributions! Please see CONTRIBUTING.md for details.

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links
Documentation: https://data-analyzer.readthedocs.io

Issue Tracker: https://github.com/intelingzhi/data-analyzer/issues

Changelog: CHANGELOG.md

## 👥 Maintainers
@intelingzhi
