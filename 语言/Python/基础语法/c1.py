
list1 = []
def create_list(file1):
    for line in file1:
        list1.append(line)
    return list1

def row(list1):
    for number in range(0,len(list1)):
        for j in range(0,len(list1)):
            if list1[number] > list1[j]:
                list1[number],list1[j] = list1[j],list1[number]
    return list1

def go(file1):
    list1 = create_list(file1)
    list1 = row(list1)
    for i in range(0,3):
        print(list1[i])


import os
os.chdir('data')
data1 = open('Bob.txt')
data2 = open('Tom.txt')
data3 = open('Lily.txt')
go(data1)
go(data2)
go(data3)