# scripts/guardrails.py
import subprocess

def run_guardrails(file_path):
    """
    Run formatting, linting, and security scans on generated code.
    """
    print(f"Running guardrails on {file_path}...")
    subprocess.run(["black", file_path])
    subprocess.run(["flake8", file_path])
    subprocess.run(["bandit", "-r", file_path])
    print("Guardrails completed.\n")