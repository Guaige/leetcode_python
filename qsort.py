import numpy as np

def qsort(left, right):
    if left>right:
        return
    i, j, t = left, right, l[left]
    while i<j:
        while i<j and t<=l[j]:
            j-=1
        while i<j and t>=l[i]:
            i+=1
        if i<j:
            l[i], l[j] = l[j], l[i]
    l[left] = l[i]
    l[i] = t
    qsort(left, i-1)
    qsort(i+1, right)

l = np.random.randint(0,100,10)
qsort(0, len(l)-1)
print(l)