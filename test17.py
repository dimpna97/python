import re
p = re.compile('[a-z]+')

m = p.match("조사할 문자열")
if m:
    print('Match found: ', m.group())
else:
    print('No match')
        
#print(m)

result = p.findall("life is too short")
print(result)

answer = p.finditer("life is too short")
print(result)
for r in result: print(r)

print(36/2.5)