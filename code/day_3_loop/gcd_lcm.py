"""
input two positive integers and return their GCD and LCM

Date: 09/26/2019
Author: Mingrui Dong
"""
# coding:utf-8


def get_gcd_lcm(number_1, number_2):
    if number_1 < number_2:
        number_1, number_2 = number_2, number_1
    for i in range(number_2, 0, -1):
        if (number_1 % i == 0) and (number_2 % i == 0):
            print("The GCD of the two numbers is %d." % i)
            print("The LCM of the two numbers is %d." % (number_1 * number_2 // i))
            return


if __name__ == '__main__':
    x = int(input("The first number:"))
    y = int(input("The second number:"))
    get_gcd_lcm(x, y)