#Q1
a = (80+75+55)/3
print(a)

#Q2
if 13%2==0:
    print("짝수")
else:
    print("홀수")
    
#Q3
pin = "881120-1068234"
yymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yymmdd)
print(num)

#Q4
pina = "881120-1068234"
print(pina.split("-")[1][0])

#Q5
b = [1,3,5,4,2]
b.sort()
b.reverse()
print(b)

#Q6
c = "a:b:c:d"
d = c.replace(":","#")
print(d)

#Q7
e =['Life', 'is', 'too', 'short']
result = ' '.join(e)
print(result)

#Q8
abc = (1,2,3)
ac = (4,)
aaaaa = abc + ac
print(aaaaa)

#Q10
x = {'A':90,'B':80, 'C':70}
print(x['B'])

#Q11
r = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(r)
n = list(aSet)
print(n)

#Q12
t = [1,2,3]
y = t[:]
t[1] = 4
print(y)

#Q9 다시 생각해보기