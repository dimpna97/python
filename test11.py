class Person: pass
a = Person()
b = 3
print(isinstance(b,Person))

c = list("python")
print(c)

# two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_(x): return x*2

print(list(map(two_,[1,2,3,4])))  
list(map(lambda a: a*2,[1,2,3,4]))

print(max([1,2,3]))
print(min("python"))

ord('a')
pow(2,4)
print(3**2)

print(list(zip([1,2,3],[4,5,6])))

import calendar
print(calendar.prmonth(2022,3))

import random
random.random(1,10)