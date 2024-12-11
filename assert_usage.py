#!/usr/bin/env python3
import sys

# make use of assert keyword
try:
	x = 1
	# it is used during developement to evaluate certain condition
	assert x > 0 , 'x must be greater than 0'

	y = "welcome"
	#if condition returns False, AssertionError is raised:
	assert y == "hello", "x should be 'hello'"

except AssertionError as e:
	print(e)
