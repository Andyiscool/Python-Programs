print ("******1")
def quicksort(array):
    if len(array) < 2:
        print ("******1")
        return array
        print ("******1")
    else:
        print ("******1")
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]
        

        return quicksort(less) + [pivot] + quicksort(greater)
    print (quicksort([10, 5, 2, 3]))
