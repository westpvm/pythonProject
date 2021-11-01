from random import randrange
n = int(input('Enter number (default: 10) : ') or 10)
a = [randrange(0, 9) for i in range(n)]
print(a)
