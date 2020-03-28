
List1 = [3,8,8,8]
i = 0
def sum(li):
    som = 0
    if len(li) == 1:
        return som+li[i]
    som = som + li.pop()
    return som + sum(li)

print(sum(List1))


def find_max(li):
    if len(li) == 0:
        return None
    if len(li) == 1:
        #此为基线条件
        return 
        
    if li[0] >= li[len(li)-1]:
        li.pop()
        find_max(li)
    else:
        li[0], li[len(li)-1] = li[len(li)-1], li[0]
        li.pop()
        find_max(li)
    return li[0]


List2 = [2,3,46,1,2,3,90]
List2 = find_max(List2)
print(List2)

import time
a = time.time()
def quicksort(array):
    if len(array) < 2:
        return array
    standard = array[0]
    small = [i for i in array[1:] if i <= standard]
    big = [j for j in array[1:] if j > standard]
    return quicksort(small) + [standard] + quicksort(big)

print(quicksort([2,7,4,8,2,7,1,0,8,5]))
print(time.time() - a)

a = time.time()
def quicksort(array):
    if len(array) < 2:
        return array
    standard = array[(len(array)//2)]
    small = [i for i in array[1:] if i <= standard]
    big = [j for j in array[1:] if j > standard]
    return quicksort(small) + [standard] + quicksort(big)

print(quicksort([2,7,4,8,2,7,1,0,8,5]))
print(time.time() - a)