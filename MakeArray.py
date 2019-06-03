import random


def randomArray(emptyArray, dimension):
    for i in range(0, dimension + 1):
        emptyArray.append(i)
    random.shuffle(emptyArray)
    return emptyArray


def casoMiglioreInsertion(emptyArray, dimension):
    for i in range(0, dimension + 1):
        emptyArray.append(i)
    return emptyArray


def casoPeggioreInsertion(emptyArray, dimension):
    for i in range(0, dimension + 1):
        emptyArray.append(i)
    reversed(emptyArray)
    return emptyArray
