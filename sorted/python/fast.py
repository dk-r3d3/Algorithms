# Быстрая сортирвока
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] # элементы меньше первого
        greater = [i for i in array[1:] if i > pivot] # элементы больше первого
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort(array=[4, 0, -1, 8, 1, 9, 12, 4, 6]))
