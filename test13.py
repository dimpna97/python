def GuGu(n):
    result = []
    i = 1
    while i <10:
        result.append(n*i)
        i = i+1
    return result

print(GuGu(3))



answer = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 ==0:
       answer += i
print(answer)            