# def is_even(n):
#     return n%2==0
from functools import reduce
lst = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda n:n%2==0,lst))
doubles = list(map(lambda n:n*2,lst))
sum  = reduce(lambda a,b:a+b,doubles)

print(sum)