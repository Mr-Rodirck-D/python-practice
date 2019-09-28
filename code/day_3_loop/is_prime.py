"""
prime judgement

Date: 09/26/2019
Author: Mingrui Dong
"""
# coding:utf-8

from math import sqrt


def is_prime(number):
    if number <= 1:
        print("The number must be greater than 1.")
        return
    end = int(sqrt(number))
    for divider in range(2, end + 1):
        if number % divider == 0:
            print("This number is not a prime")
            return
    print("This number is a prime")
    return


if __name__ == '__main__':
    number = int(input("Please input a number:"))
    is_prime(number)
