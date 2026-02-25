# agents/code_agent.py
def generate_feature_code(feature_request):
    """
    Mock AI agent: returns Python code for requested feature.
    Replace this with OpenAI API later if desired.
    """
    fr = feature_request.lower()
    
    if "factorial" in fr:
        return """def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
"""
    elif "prime" in fr:
        return """def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
"""
    elif "reverse" in fr:
        return """def reverse_string(s):
    return s[::-1]
"""
    elif "fizzbuzz" in fr:
        return """def fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result
"""
    elif "word frequency" in fr:
        return """def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
"""
    else:
        return f"# Feature code for: {feature_request}\n"