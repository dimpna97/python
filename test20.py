import random

def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) -index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
                
        if swap == False:
            break
    return data

data_list = random.sample(range(100),50)
print(bubblesort(data_list))


def insertion_sort(data):
    for index in range(len(data) -1):
        for index2 in range(index +1,0,-1):
            if data[index2] < data[index2 -1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break
    return data
 