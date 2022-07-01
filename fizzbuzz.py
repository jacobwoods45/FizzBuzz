"""
"Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
"""
def generate_numbers():
    i = 0
    while i <= 100:
        check_number(i)
        i = i + 1
def check_number(number):
    if number % 3  == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
generate_numbers()