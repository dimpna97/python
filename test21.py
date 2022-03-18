import string
from typing_extensions import _AnnotatedAlias


def factorial(num):
    if num > 1:
      return num * factorial(num-1)
    else:
        return num
    
for num in range(10):
    print(factorial (num))
    
def factorial1(num):
    if num <=1:
        return num
    return_value = num * factorial1(num-1)
    return return_value

for num in range(10):
    print(factorial1(num))
    
    
def multiple(num):
    return_value = 1
    for index in range(1,num+1):
        return_value = return_value * index
    return return_value

def multiple(num):
    if num <=1:
       return num
    return num * multiple(num-1)

print(multiple(10)) 

data = [17,16,65,49,88,15,99,45,77,87]

def sum_list(data):
    if len(data)<=1:
        return data[0]
    return data[0] + sum_list(data[1:])

print(sum_list(data))

#회문은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함

def palindrome(string):
    if len(string) <=1:
        return True
    
    if string[0] ==string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
string = "anana"
print(palindrome(string))
    

def func(n):
    print(n)
    if n==1:
      return n
  
    if n%2==1:
      return(func(3*n)+1)
    else:
      return(func(int(n/2)))
  
print(func(3))