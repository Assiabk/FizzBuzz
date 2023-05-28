# FizzBuzz: Write a program that prints the numbers from 1 to 100. For multiples of three, 
# print "Fizz" instead of the number. For multiples of five, print "Buzz" instead of the number.
# For numbers that are multiples of both three and five, print "FizzBuzz".
for num in range(101):
    if num % 3==0 and num % 5== 0:
        print(" FizzBuzz") 
    elif num % 3==0:
        print("fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)