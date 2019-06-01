import InsertionSort as ins
import MergeSort as mrg
import random
import time
import matplotlib.pyplot as plt
import numpy as np


insertionTime = []
mergeSortTime = []
for j in range(100, 10000, 50):
    print("Parliamo di ", j, "/", 10000, "%", j/100)
    A = []
    for i in range(0, j):
        A.append(random.randint(0, 10000))
    B = A[:]

    # InsertionSort
    startTime = time.time()
    ins.insertionsort(A)
    insertionTime.append(time.time() - startTime)

    # MergeSort
    startTime = time.time()
    mrg.mergesort(B, 1, len(B))
    mergeSortTime.append(time.time() - startTime)

t = np.arange(0, len(mergeSortTime))
plt.plot(t, insertionTime)
plt.plot(t, mergeSortTime)
plt.xlabel('Dimensione Array')
plt.ylabel('Tempo')
plt.grid()
plt.show()
plt.savefig("grafico.png")


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