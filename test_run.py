from agents.code_agent import generate_feature_code

feature_request = "Write a function to check if a number is prime"
code = generate_feature_code(feature_request)

print("Generated code:\n", code)

# Save to features folder
file_map = {
    "factorial": "features/factorial.py",
    "prime": "features/is_prime.py",
    "reverse": "features/reverse_string.py",
    "fizzbuzz": "features/fizzbuzz.py",
    "word frequency": "features/word_frequency.py"
}

for key, path in file_map.items():
    if key in feature_request.lower():
        with open(path, "w") as f:
            f.write(code)
        print(f"Code saved to {path}")