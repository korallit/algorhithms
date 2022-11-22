
def swapelements(lista, index):
    nextelement = lista[index+1]
    if lista[index] > lista[index+1]:
        lista[index], lista[index+1] = nextelement, lista[index]


def firstiteration(lista, length):
    for i in range(0, length-1):
        swapelements(lista, i)


def bubblesort(lista):
    i = len(lista)
    while i > 0:
        firstiteration(lista, i)
        i -= 1
