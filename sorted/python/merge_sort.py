# Сортировка слиянием
def merge_sort(array):
    if len(array) > 1:
        mind = len(array) // 2 # срез
        left = array[:mind]
        right = array[mind:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

list1 = [1, 4, -1, 0, 4, 5, 2, 10, 9, 11]
merge_sort(list1)
print(list1)


