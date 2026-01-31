from functools import reduce
num = [x for x in range(10)]
sqr = list(map(lambda x: x**2,num))
even = list(filter(lambda x:x%2==0,sqr))
sum_Even = reduce(lambda x,y:x+y,even)
print("Squared:",sqr)
print("Even:",even)
print("Sum:",sum_Even)