#!/usr/bin/env python3

def happy_new_year():
    i = 1
    while i < 11:
        print(i)
        i += 1
    else:
        print("Happy New Year")
happy_new_year()

def square_integers(int_list):
    return [x*x for x in int_list]
print(square_integers([1, 2, 3]))


def fizzbuzz(num):
   i = 1
   while i < 101:
       if i % 3 == 0 and i % 5 == 0:
           print("FizzBuzz")
       elif i % 3 == 0:
           print("Fizz")
       elif i % 5 == 0:
           print("Buzz")
       else:
           print(num)
fizzbuzz()
