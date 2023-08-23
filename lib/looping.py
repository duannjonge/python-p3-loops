#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count=11
    while(count<=11 and count >1):
        count -= 1
        print(count)
    if count ==1:
        print("Happy New Year!")
      

happy_new_year()

def square_integers(int_list):
    # code goes here!
    value= int(int_list)
    print(value)
    return str(value **2)

square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function to print FizzBuzz from 1 to 100
fizzbuzz()

