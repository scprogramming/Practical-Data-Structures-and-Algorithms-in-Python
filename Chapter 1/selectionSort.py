def selectionSort(listIn):

    for i in range(len(listIn)):
        nextSmallest = i
        for j in range(i+1,len(listIn)):
            if listIn[nextSmallest] > listIn[j]:
                nextSmallest = j

        listIn[i], listIn[nextSmallest] = listIn[nextSmallest], listIn[i]

    return listIn

listToSort = [4, 2, 5, 1, 9]

print(selectionSort(listToSort))