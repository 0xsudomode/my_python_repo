#!/usr/bin/env python3

import argparse


def add_two(num1,num2):
    return f'[+] addition result: {num1+num2}'

parser = argparse.ArgumentParser(description='adding two numbers nothing fnacy :p')

parser.add_argument('-n1','--number1',type=int, metavar= '', required=True, help='enter the first number')
parser.add_argument('-n2','--number2',type=int, metavar= '', required=True, help='enter the second number')

args = parser.parse_args()

if __name__ == '__main__':
    print(add_two(args.number1,args.number2))
    #print(args)
