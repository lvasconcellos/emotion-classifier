# Emotion Classifier

This project provides a simple, pre-trained AI model for emotion classification based on text input. The goal is to create a **clean, reusable**, and **open-source** implementation before customizing it for specific use cases.

## Features
- Uses a **Hugging Face** pre-trained model for emotion classification.
- Supports **virtual environment (venv)** for dependency management.
- Enforces **code quality** with pre-commit hooks (Black, Flake8, MyPy, etc.).
- **GitHub Actions** CI workflow for automated checks.

## Setup Guide

### 1. Clone the Repository
```bash
git clone <repo-url>
cd emotion-classifier
```

### 2. Create and Activate Virtual Environment
#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### Mac/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up Pre-commit Hooks
```bash
pre-commit install
```
To manually run pre-commit checks on all files:
```bash
pre-commit run --all-files
```

### 5. Run Emotion Classification
```bash
python -m src.main "Your journal entry text here"
```

## Contribution Guidelines
- Ensure pre-commit hooks pass before committing.
- Follow **SOLID, DRY, and clean architecture** principles.
- Use **meaningful commit messages**.

## License
This project is open-source and available under the **MIT License**.
