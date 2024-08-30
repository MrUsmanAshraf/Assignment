name: str= str(input("Enter your name: "))
numbers = []
for number in range (3):
    number=int(input(f"Enter your favorite number : "))
    numbers.append(number)
print(f"Hello, {name} Let's explore your favorite numbers.")
for number in numbers:
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
for number in numbers:
    print(f"the number {number} and its square is: {number, number **2}")
numbers_sum =(sum(numbers))
print(f"Amazing! the sum of your favorite numbers is:  {numbers_sum}.")
from sympy import isprime
if isprime(numbers_sum):
    print(f"{numbers_sum} is a prime number.")
else:
    print((f"{numbers_sum} is not a prime number."))