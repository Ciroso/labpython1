import InsertionSort as ins
import MergeSort as mrg
import time
import matplotlib.pyplot as plt
import numpy as np
import MakeArray


tempoTotale = time.time()
insertionTimeMigliore = []
insertionTimePeggiore = []
insertionTime = []
mergeSortTime = []
dimension = 5000
for j in range(100, dimension, 500):
    print("Parliamo di ", j, "/", dimension, "%", j/50, end=' e ci mette ')
    tempoTempo = time.time()
    A = []
    A = MakeArray.randomArray(A, j)
    B = A[:]
    tempoTempo = time.time()-tempoTempo
    print(tempoTempo)

    # InsertionSort
    startTime = time.time()
    ins.insertionsort(A)
    insertionTime.append(time.time() - startTime)

    # Miglior InsertioSort
    startTime = time.time()
    ins.insertionsort(A)
    insertionTimeMigliore.append(time.time() - startTime)

    # Peggior InsertionSort
    A = MakeArray.casoPeggioreInsertion(A)
    startTime = time.time()
    ins.insertionsort(A)
    insertionTimePeggiore.append(time.time() - startTime)

    # MergeSort
    startTime = time.time()
    mrg.mergesort(B, 1, len(B))
    mergeSortTime.append(time.time() - startTime)

t = np.arange(0, len(mergeSortTime))
print(100, "%!!!!!!!")
plt.plot(t, insertionTime, label="InsertionSort")
plt.plot(t, insertionTimePeggiore, label="WorstInsertionSort")
plt.plot(t, mergeSortTime, label="MergeSort")
plt.legend()
plt.xlabel('Dimensione Array')
plt.ylabel('Tempo')
plt.grid()
plt.draw()
plt.savefig('grafico.png', dpi=100)
plt.show()
print("Ci abbiamo impiegato ", time.time() - tempoTotale)
