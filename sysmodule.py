import sys

print(f'python version : {sys.version}')

sys.stdout.write('this is written without using print function\n')

sys.stderr.write('this is an error from stderr.')

print(f'platform : {sys.platform}')

print("Maximum integer size:", sys.maxsize)

num = 100
print("Size of integer 100:", sys.getsizeof(num), "bytes")

text = "Hello, world!"
print("Size of string:", sys.getsizeof(text), "bytes")

print("sys module:", sys.modules['sys'])

print("Byte order:", sys.byteorder)

print("Python executable path:", sys.executable)

sys.exit(0) # 0 successful termination 1 otherwise.

# there are more functions , this is just a tiny demo.


