import random

def createCard():

    card = set()

    while True:
        num = random.randint(1, 91)

        card.add(num)

        numOfSet = len(card)

        if numOfSet == 15:
            break
        else:
            pass

    return card




def displayCard(card):
    row = []
    row1 = []
    row2 = []

    numLists = 3

    lists = [row, row1, row2]

    for i, number in enumerate(card):
        list_index = i % numLists  # Вычисляем индекс списка, в который нужно перенести число
        lists[list_index].append(number)

    row = sorted(row)
    row1 = sorted(row1)
    row2 = sorted(row2)

    n = 6

    for i in range(4):
        b = random.randint(1, n)
        elemAdd = row.insert(b, "[ ]")
        b = random.randint(1, n)
        elemAdd = row1.insert(b, "[ ]")
        b = random.randint(1, n)
        elemAdd = row2.insert(b, "[ ]")
        n = n + 1

    v = "-" * 50

    card = (f'{v}\n {row}\n {row1}\n {row2}\n {v}')

    #print(rowOrig)
    print(card)

playerCard = createCard()
displayCard(playerCard)
