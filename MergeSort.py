import sys


def mergesort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    L = []
    R = []
    n1 = q - p + 1
    n2 = r - q
    for i in range(n1):
        L.append(A[p + i - 1])
    for j in range(n2):
        R.append(A[q + j])
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = 0
    j = 0
    for k in range(p-1, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
