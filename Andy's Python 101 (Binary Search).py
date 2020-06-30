
def binary_search (my_list, item):
    low = 0
    count = 0
    high = len(my_list)-1
    while low <= high:
        mid = int((low + high) / 2)
        guess = my_list[mid]
        count = count + 1
        if guess == item:
            print("count = " + str(count))
            return mid
          
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    print("count = " + str(count))

    return None
my_list = [1, 3, 5, 7, 9, 11, 13, 15]

print (binary_search(my_list, 7)) # => 1
print (binary_search(my_list, 15)) # => None


