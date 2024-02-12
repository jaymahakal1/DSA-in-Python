# improved version of Insertion sort

def ShellSort(arr : list):
    h = int(input('Enter maximum Increment : '))
    while h > 0:
        for i in range(h, len(arr)):
            temp = arr[i]
            j = i-h
            while j >= 0 and arr[j] > temp:
                arr[j+h] = arr[j]
                j = j - h
            arr[j + h] = temp
        h -= 2
    return arr

a = [5,3,5,2,7]
ShellSort(a)
print(a)
