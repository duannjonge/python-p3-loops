#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count=10
    while(count<=10 and count >=1):
       
        print(count)
        count -= 1
    print("Happy New Year!")
      

happy_new_year()

def square_integers(int_list):
    # code goes here!
    new_list=[]
    for n in int_list:
        new_list.append(n * n)
    return new_list
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

