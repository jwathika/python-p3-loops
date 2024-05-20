#!/usr/bin/env python3


def happy_new_year():
    year = 0
    while year < 10:
        year += 1
        print(year)
        print("Happy New Year!")


def square_integers(int_list):
    squared_list = []
    for i in int_list:
        new_i = i * i
        squared_list.append(new_i)
        print(new_i)
    return squared_list


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
