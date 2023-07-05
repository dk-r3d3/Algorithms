# сортировка пузырьком на питоне

def buble_sorted(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]

array = [3, 1, 5, 0, 7, 2, 5]
buble_sorted(array)
print(array)