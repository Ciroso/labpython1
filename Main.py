import InsertionSort as ins
import MergeSort as mrg
import random
import time

A = []
for i in range(0, 60000):
    A.append(random.randint(0, 100000))
B = A[:]
startTime = time.time()
ins.insertionsort(A)
elapsedTime = time.time() - startTime
print("Insertionsorted ", elapsedTime)
startTime = time.time()
mrg.mergesort(B, 1, len(B))
elapsedTime = time.time() - startTime
print("Mergessorete ", elapsedTime)
if A == B:
    print("E sono pure uguali!")
