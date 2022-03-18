a = 0
while a<10:
    a = a+1
    if a%3==0: continue
    print(a)
    

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
    
aa = [(1,2), (3,4), (5,6)]
for (first, last) in aa:
    print(first + last)
    
#marks1.py
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
     print("%d번 학생은 합격입니다." % number)
    else:
     print("%d번 학생은 불합격입니다." % number)
     
# marks2.py
markss = [90,25,67,45,80]
num = 0
for marking in markss:
    num = num +1
    if marking<60 : continue
    print("%d번 학생 축하합니다. 합격입니다." % num)

b = range(1,10)
print(b)

add = 0
for i in range(1,11):
    add = add + i
print(add)