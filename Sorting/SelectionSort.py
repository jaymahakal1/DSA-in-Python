def SelectionSort(arr : list):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n,1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


a = [5,3,5,2,7]
print(SelectionSort(a))

# unstable sort
# In place sort
# Stable sort ==> relative order of elements doesn't change
# in-place sort ==> they dont require extra storage
# e.g. ==> Selection sort, Insertion Sort, Bubble Sort, shell sort
# not-in place ==> they require xtra space just like merge sort