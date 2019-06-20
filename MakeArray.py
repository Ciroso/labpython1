import random


def randomArray(emptyArray, dimension):
    for i in range(0, dimension + 1):
        emptyArray.append(i)
    random.shuffle(emptyArray)
    return emptyArray


def casoPeggioreInsertion(emptyArray):
    list.reverse(emptyArray)
    return emptyArray
