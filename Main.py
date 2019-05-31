import InsertionSort as ins
import MergeSort as mrg
import random
import time
import matplotlib.pyplot as plt
import numpy as np


def getInsertionTime(t):
    return insertionTime[t]


insertionTime = []
mergeSortTime = []
n = 100
A = []
for j in range(n):
    print(j)
    for i in range(0, 600):
        A.append(random.randint(0, 100000))

    B = A[:]

    startTime = time.time()
    ins.insertionsort(A)
    elapsedTime = time.time() - startTime
    print("Insertionsorted ", elapsedTime)
    insertionTime.append(elapsedTime)


    startTime = time.time()
    mrg.mergesort(B, 1, len(B))
    elapsedTime = time.time() - startTime
    mergeSortTime.append(elapsedTime)
    print("Mergessorete ", elapsedTime)

t = np.arange(0, len(insertionTime))
plt.plot(t, insertionTime)
plt.plot(t, mergeSortTime)
plt.xlabel('numero dati')
plt.show()

'''
import numpy as np import matplotlib.pyplot as plt
# Seno e coseno 
x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)
# usiamo matplotlib 
plt.plot(x, y_sin) 
plt.plot(x, y_cos) 
plt.xlabel(’x axis label’) 
plt.ylabel(’y axis label’) 
plt.title(’Sine and Cosine’) 
plt.legend([’Sine’, ’Cosine’]) 
plt.show(
'''