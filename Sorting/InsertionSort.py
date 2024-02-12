def insertionSort(arr : list):
    n = len(arr)
    for i in range(1,n,1):
        j = i-1
        cur_key = arr[i]
        while j >= 0 and arr[j] > cur_key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur_key
    return arr

# key idea is to place each element in its correct position considering left part from the cur_element(except cur_ele) is sorted and right part 
# including the cur_ele is unsorted

# a = [5,3,5,2,7]
# print(insertionSort(a))

# in-place
# stable sort