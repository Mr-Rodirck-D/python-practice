"""
find all perfect numbers from 1 to 10000

Date: 09/26/2019
Author: Mingrui Dong
"""
# coding:utf-8


from math import sqrt


def is_perfect_number(number):
    divisor = []
    total = 0
    for k in range(1, int(sqrt(number)) + 1):
        if number % k == 0:
            divisor.append(k)
            if k != sqrt(number):
                divisor.append(number / k)
    for j in divisor:
        total = total + j
    total = total - number
    # print("total of %d is: %d" % (number, total))
    if total == number:
        return True
    else:
        return False


if __name__ == '__main__':

    for i in range(1, 10000):
        if is_perfect_number(i):
            print("Perfect number: %d" % i)
