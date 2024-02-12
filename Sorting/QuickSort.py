def partition(v, lo, hi):
    p = v[lo]
    i = lo + 1
    j = hi

    while i <= j:
        if v[i] > p and v[j] < p:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
        if v[i] <= p:
            i += 1

        if v[j] >= p:
            j -= 1
    v[lo], v[j] = v[j], v[lo]
    return j



def QuickSort(v, lo, hi):
    if lo < hi : 
        mid = lo + (hi - lo) // 2
        pivot = partition(v, lo, hi)

        QuickSort(v, lo, pivot - 1)
        QuickSort(v, pivot + 1, hi)


a = [5,3,5,2,7]
n = len(a)
QuickSort(a, 0, n-1)
print(a)

''' 
in place algo
 best - O(nlogn)
 worst - O(n^2)
 It is efficient on large data sets.
 It has a low overhead, as it only requires a small amount of memory to function.
 o(1) space
'''