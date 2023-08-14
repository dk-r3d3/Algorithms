# пирамиадльная (кучей)

def diff(collection, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and collection[i] < collection[left]:
        largest = left

    if right < n and collection[largest] < collection[right]:
        largest = right

    if largest != i:
        collection[i],arr[largest] = collection[largest],collection[i]

        diff(collection, n, largest)

def ResSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        diff(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        diff(arr, i, 0)

arr = [int(input()) for _ in range(10)]
ResSort(arr)
n = len(arr)

print(arr)
