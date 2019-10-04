import InsertionSort as ins
import MergeSort as mrg
import time
import matplotlib.pyplot as plt
import MakeArray


finalInsertionTime = []
finalWorstInsertionTime = []
finalMergeSort = []
finalReverseMergeSort = []

insertionTimePeggiore = []
insertionTime = []

mergeSortTime = []
mergeSortTimeReverse = []

nodeCounter = []
dimension = 5000
repetition = 10
step = -1
for j in range(100, dimension, 250):
    step += 1
    print("Parliamo di ", j, "/", dimension, "%", j*100/dimension)
    insertionTimePeggiore = []
    insertionTime = []
    mergeSortTime = []
    mergeSortTimeReverse = []

    for i in range(repetition):
        A = []
        A = MakeArray.randomArray(A, j)
        B = A[:]

        # InsertionSort medio
        startTime = time.time()
        ins.insertionsort(A)
        insertionTime.append(time.time() - startTime)

        # MergeSort medio
        startTime = time.time()
        mrg.mergesort(B, 1, len(B))
        mergeSortTime.append(time.time() - startTime)

        A = MakeArray.casoPeggioreInsertion(A)
        B = A[:]

        # Peggior InsertionSort
        startTime = time.time()
        ins.insertionsort(A)
        insertionTimePeggiore.append(time.time() - startTime)

        # MergeSort reverse
        startTime = time.time()
        mrg.mergesort(B, 1, len(B))
        mergeSortTimeReverse.append(time.time() - startTime)

    tempInsTime = 0
    tempWorstInsTime = 0
    tempMergeSortTime = 0
    tempReverseMergeSortTime = 0
    for w in range(repetition):
        tempInsTime += insertionTime[w]
        tempWorstInsTime += insertionTimePeggiore[w]
        tempMergeSortTime += mergeSortTime[w]
        tempReverseMergeSortTime += mergeSortTimeReverse[w]
    finalInsertionTime.append(tempInsTime/repetition)
    finalWorstInsertionTime.append(tempWorstInsTime/repetition)
    finalMergeSort.append(tempMergeSortTime/repetition)
    finalReverseMergeSort.append(tempReverseMergeSortTime/repetition)

    nodeCounter.append(j)
# t = np.arange(0, len(mergeSortTime))
print(100, "%!!!!!!!")

# WorstCase
plt.plot(nodeCounter, finalWorstInsertionTime, label="InsertionSort worst")
plt.plot(nodeCounter, finalReverseMergeSort, label="MergeSort with the same data")
plt.legend()
plt.xlabel('Dimensione Array')
plt.ylabel('Tempo')
plt.grid()
plt.draw()
plt.savefig('Caso peggiore.png', dpi=100)
plt.show()

# Awerage case
plt.plot(nodeCounter, finalInsertionTime, label="InsertionSort")
plt.plot(nodeCounter, finalMergeSort, label="MergeSort")
plt.legend()
plt.xlabel('Dimensione Array')
plt.ylabel('Tempo')
plt.grid()
plt.draw()
plt.savefig('Caso medio.png', dpi=100)
plt.show()
