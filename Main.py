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
for j in range(100, 10000, 50):
    print("Parliamo di ", j, "/", 10000, "%", j/100, end=' e ci mette ')
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
plt.plot(t, insertionTime)
plt.plot(t, mergeSortTime)
plt.plot(t, insertionTimePeggiore, linestyle='', marker='*')
plt.xlabel('Dimensione Array')
plt.ylabel('Tempo')
plt.grid()
plt.draw()
plt.savefig('grafico.png', dpi=100)
plt.show()
print("Ci abbiamo impiegato ", time.time() - tempoTotale)

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