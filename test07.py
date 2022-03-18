#marks3.py
marks = [90,25,67,45,80]
for i in range(len(marks)):
    if marks[i] <60: continue
    print("%d번 학생 축하합니다. 합격입니다." %(i+1))

num = 0    
for i in range(1,101):
    num = num + i
print(num)

for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %d" % (i,j,i*j), end=" ")
    print('')
    
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)        


abc = [1,2,3,4]
result = [number * 3 for number in abc if number % 2 == 0]

print(result)        