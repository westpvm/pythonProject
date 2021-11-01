from random import randrange
my_list = [randrange(0, 11) for n in range(10)]
print(my_list)
b = int(input("Enter num: "))
print(b)
indices = [i for i, x in enumerate(my_list) if x == b]
print('Number', b, 'is listed under number:', indices)
