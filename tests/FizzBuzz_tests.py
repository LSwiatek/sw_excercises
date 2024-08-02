def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n



def test_returnsNumber():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(15) == "FizzBuzz"


def test_returnsBuzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(25) == "Buzz"
    assert fizzbuzz(100) == "Buzz"

