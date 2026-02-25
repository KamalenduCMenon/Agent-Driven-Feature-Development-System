from features.fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(3)[-1] == "Fizz"
    assert fizzbuzz(5)[-1] == "Buzz"
    assert fizzbuzz(15)[-1] == "FizzBuzz"