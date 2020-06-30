def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        smallest = arr[i]
        smallest_index = i
    return smallest_index
print ("*******1")
def selectionSort (arr):
    newArr = []
    for i in range (len(arr)):
        smallest = findSmallest (arr)
        newArr.append (arr.pop(smallest))
        print ("*******2")
    return newArr

print (selectionSort([5, 3, 6, 2, 10, 11, 15]))
