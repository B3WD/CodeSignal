import time
import numpy as np

np.random.seed(124)
randnums = np.random.randint(1, int(1e9), int(1e5))

def firstDuplicate1(a):
    minSecInd = len(a)
    isFound = False

    for i, n in enumerate(a):
        for j in list(range(i+1, len(a))):
            if n == a[j] and j < minSecInd:
                minSecInd = j
                isFound = True
        
    if isFound:
        return a[minSecInd]
    return -1


def firstDuplicate2(a):
    lenA = len(a)
    minSecInd = lenA
    isFound = False
    num = a[0]

    for i, n in enumerate(a):
        if n == None:
            continue

        for j in range(i+1, lenA):
            if n == a[j] and j < minSecInd:
                minSecInd = j
                isFound = True
                num = a[j]
                a[j] = None
                break
        
    if isFound:
        return num
    return -1


def firstDuplicate3(a):
    l, r = 0, len(a) 
    isFound = False

    for i in range(l, r):

        if len(set(a[l:r])) == len(a[l:r]) and not isFound:
            return -1

        for j in range(l + 1, r):
            if(a[i] == a[j]):
                r = j
                isFound = True
                break
        l = i + 1

    if isFound:
        return a[r]
    return -1


def firstDuplicate4(a):
    sa = list(dict.fromkeys(a))
    szSet = len(sa)
    szA = len(a)
    i = 0

    if(szSet == szA):
        return -1

    for _ in range(szSet):
        if sa[i] != a[i]:
            return a[i]
        i += 1

    if i == szA:
        return -1
    else:
        return a[i]


randnums = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]

print("v4")
a = list(randnums)

t0 = time.perf_counter()
res = firstDuplicate4(a)
t1 = time.perf_counter()

total = t1-t0
print(total)

print(res)

#===============================

print("v3")
a = list(randnums)

t0 = time.perf_counter()
res = firstDuplicate3(a)
t1 = time.perf_counter()

total = t1-t0
print(total)

print(res)

#===============================

print("v2")
a = list(randnums)

t0 = time.perf_counter()
res = firstDuplicate2(a)
t1 = time.perf_counter()

total = t1-t0
print(total)

a = list(randnums)
print(res)

#==============================

print("v1")
a = list(randnums)

t0 = time.perf_counter()
res = firstDuplicate1(a)
t1 = time.perf_counter()

total = t1-t0
print(total)

print(res)