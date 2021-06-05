def insertionSort(listIn):
    for i in range(1, len(listIn)):
        key = listIn[i]

        j = i - 1
        while j >= 0 and key < listIn[j]:
            listIn[j + 1] = listIn[j]
            j -= 1

        listIn[j + 1] = key

    return listIn


listToSort = [4, 2, 5, 1, 9]

print(insertionSort(listToSort))