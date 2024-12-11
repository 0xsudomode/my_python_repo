#!/usr/bin/env python3

# treat user input as hex
print('input data ex : 49 59 69')

# used lambda to treat input as hex
input_hex = list(map(lambda x: bytes.fromhex(x),input().split()))

# latin-1 to handle non printable hex values
print('ASCII/LATIN representation : ' + ' '.join([b.decode('latin-1') for b in input_hex]))

print('input string ex : H E L L O')
data = input().split()
input_str = list(map(ord,data)) 
# map (function , iterable) -> used to apply a given function to every item of an iterable

print(f"Decimal representation {' '.join(map(str,input_str))}")
