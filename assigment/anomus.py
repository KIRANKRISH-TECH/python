# x=lambda a:a+10
# print(x(5))



# x=lambda a, b: a + b
# print(x(5, 10))


# x=lambda a, b: a * b
# print(x(5, 10))


# x=lambda a, b, c: a + b + c
# print(x(5, 10, 15))



# .........................maping

# numbers = [1, 2, 3, 4, 5]
# squared_numbers =list(map(lambda x:x*2,numbers))
# print(squared_numbers)



# ....................filter

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
# print(even_numbers)



# ....................reduce

from functools import reduce    
numbers = [1, 2, 3, 4]         
product = reduce(lambda x, y: x + y, numbers)
print(product)








