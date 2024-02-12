def merge(arr, l, mid, r):
    sizeofone = mid-l+1
    sizeofsecond = r-mid

    arr1 = [0 for _ in range(sizeofone)]
    arr2 = [0 for _ in range(sizeofsecond)]

    
    for i in range(sizeofone):
        arr1[i] = arr[i+l]

    for i in range(sizeofsecond):
        arr2[i] = arr[i+mid+1]

    i, j, k = 0, 0, l
    while i < sizeofone and j < sizeofsecond:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        
        k += 1

    while i < sizeofone:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < sizeofsecond:
        arr[k] = arr2[j]
        j += 1
        k += 1

def mergeSort(arr : list, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)

        merge(arr, l, mid, r)



a = [5,3,5,2,7]
n = len(a)
mergeSort(a, 0, n-1)
print(a)


# not in place sort
# Stable sort