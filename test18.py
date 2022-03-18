def hash_func(key):
    return key % 5


data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

##ord(): 문자의 ASCII(아스키)코드 리턴
##unicode
print(ord(data1[O]), ord(data2[O]), ord(data3[O]))
print(ord(data1[O]), hash_func(ord(data1[O])))

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value
    
storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

get_data('Andy')    