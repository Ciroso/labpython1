import InsertionSort as ins
import MergeSort as mrg
import time
import matplotlib.pyplot as plt
import MakeArray


tempoTotale = time.time()
insertionTimeMigliore = []
insertionTimePeggiore = []
insertionTime = []
mergeSortTime = []
mergeSortTimeReverse = []
t = []
dimension = 5000
for j in range(100, dimension, 500):
    print("Parliamo di ", j, "/", dimension, "%", j/50, end=' e ci mette ')
    tempoTempo = time.time()
    A = []
    A = MakeArray.randomArray(A, j)
    B = A[:]
    tempoTempo = time.time()-tempoTempo
    print(tempoTempo)

    # InsertionSort medio
    startTime = time.time()
    ins.insertionsort(A)
    insertionTime.append(time.time() - startTime)

    # Peggior InsertionSort
    A = MakeArray.casoPeggioreInsertion(A)
    startTime = time.time()
    ins.insertionsort(A)
    insertionTimePeggiore.append(time.time() - startTime)

    # MergeSort medio
    startTime = time.time()
    mrg.mergesort(B, 1, len(B))
    mergeSortTime.append(time.time() - startTime)

    # MergeSort peggiore
    startTime = time.time()
    mrg.mergesort(A, 1, len(A))
    mergeSortTimeReverse.append(time.time() - startTime)

    t.append(j)

#t = np.arange(0, len(mergeSortTime))
print(100, "%!!!!!!!")
# WorstCase
plt.plot(t, insertionTimePeggiore, label="InsertionSort")
plt.plot(t, mergeSortTimeReverse, label="MergeSort")
plt.legend()
plt.xlabel('Dimensione Array')
plt.ylabel('Tempo')
plt.grid()
plt.draw()
plt.savefig('Caso peggiore.png', dpi=100)
plt.show()

# Awerage case
plt.plot(t, insertionTime, label="InsertionSort")
plt.plot(t, mergeSortTime, label="MergeSort")
plt.legend()
plt.xlabel('Dimensione Array')
plt.ylabel('Tempo')
plt.grid()
plt.draw()
plt.savefig('Caso medio.png', dpi=100)
plt.show()

print("Ci abbiamo impiegato ", time.time() - tempoTotale)
