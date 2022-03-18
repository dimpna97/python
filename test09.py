def add_many(*args): #리스트 같은 존재라 생각하면 됨.. 
    result = 0
    for i in args:
        result = result + i
    return result 

result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result 

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)       


def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)
print_kwargs(name = 'foo', age = 3, bee = 'hey')

def add_and_mul(a,b):
    return a+b, a*b

re1, re2 = add_and_mul(3,4)
print(re1)
print(re2)

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)
    
say_nick('야호')
say_nick('바보')

add = lambda a, b: a+b
result = add(3,4)
print(result)

az = input("숫자입력 궈궈")
print(az)