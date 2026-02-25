from agents.code_agent import generate_feature_code
from scripts.guardrails import run_guardrails

# Features to generate
feature_requests = [
    "factorial",
    "prime",
    "reverse string",
    "fizzbuzz",
    "word frequency"
]

file_map = {
    "factorial": "features/factorial.py",
    "prime": "features/is_prime.py",
    "reverse string": "features/reverse_string.py",
    "fizzbuzz": "features/fizzbuzz.py",
    "word frequency": "features/word_frequency.py"
}

for feature_request in feature_requests:
    generated_code = generate_feature_code(feature_request)
    file_path = file_map[feature_request]
    with open(file_path, "w") as f:
        f.write(generated_code)
    print(f"Generated feature saved to {file_path}")
    run_guardrails(file_path)