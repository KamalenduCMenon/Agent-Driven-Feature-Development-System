# Agent-Driven Feature Development System

![Workflow Diagram](diagram.png)

## Overview

This project demonstrates a **mock AI agent system** that automatically generates Python code for multiple feature requests.  

Key capabilities:

- Mock AI agent generates Python features (factorial, prime check, etc.)  
- **Guardrails** for reliable code: formatting, linting, security scanning  
- **Automated tests** for each generated feature  
- Fully modular and **portfolio-ready** workflow  

---

## Features

The mock AI currently supports generating the following features:

| Feature | Description |
|---------|-------------|
| Factorial | Calculates factorial of a number |
| Prime Checker | Checks if a number is prime |
| Reverse String | Reverses a string |
| FizzBuzz | Classic FizzBuzz sequence generator |
| Word Frequency | Counts word frequency in a text |

> Each feature has a dedicated test file for automated verification.

---

## Project Structure

```text
Agent Driven Feature Development/
├── agents/                # Mock AI agent code
│   └── code_agent.py
├── features/              # Generated feature code
│   ├── __init__.py
│   ├── factorial.py
│   ├── is_prime.py
│   ├── reverse_string.py
│   ├── fizzbuzz.py
│   └── word_frequency.py
├── scripts/               # Utilities (guardrails)
│   └── guardrails.py
├── tests/                 # Automated tests
│   ├── __init__.py
│   ├── test_factorial.py
│   ├── test_prime.py
│   ├── test_reverse.py
│   ├── test_fizzbuzz.py
│   └── test_wordfreq.py
├── main.py                # Generate all features automatically
├── test_run.py            # Quick test for AI generation
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── diagram.png            # Workflow diagram
```
---

## Workflow Diagram

Steps:
- User Feature Request – The system automatically generates predefined features
- AI Agent – Mock AI generates Python code
- Guardrails – Run formatting (Black), linting (Flake8), and security scan (Bandit)
- Features Folder – Save generated code to features/
- Automated Tests – Run pytest on all generated features
- Success / Error Logs – Ensure reliable outcomes

The workflow simulates a real agent-driven development system.

---
## Tools & Technologies

- Python 3.11+
- Black – Code formatting
- Flake8 – Linting
- Bandit – Security scanning
- Pytest – Automated testing
- Git – Version control
- Mock AI agent – Simulates OpenAI API (can be replaced with real API later)

---

## Notes

- Features are predefined but system is modular for adding new features
- Guardrails ensure clean, secure, and maintainable code
- Automated tests ensure every feature works correctly