n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1,24):
    print(d[i], end=' ')    
    
    
    
num = int(input())
numlist = input().split()

numlist.reverse()
for i in range(0,num):
    print(numlist[i], end=' ')