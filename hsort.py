import numpy as np

def adjust_heap(p, len):
    t = l[p]
    i = 2*p+1
    while i<len:
        if i+1<len and l[i+1]>l[i]:
            i+=1
        if l[i]>t:
            l[p], p = l[i], i
        else:
            break
        i = 2*i+1
    l[p] = t

l = np.random.randint(0,100,10)
print(l)

for i in range(len(l)//2-1, -1, -1):
    adjust_heap(i, len(l))
for i in range(len(l)-1, 0, -1):
    l[0], l[i] = l[i], l[0]
    adjust_heap(0, i)
print(l)