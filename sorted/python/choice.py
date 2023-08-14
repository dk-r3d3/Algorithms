# Сортировка выбором
def sorted_by_choice(collection):
    size = len(collection)
    for i in range(0, size):
        position = i
        for j in range(i + 1, size):
            if collection[j] < collection[position]:
                position = j
        collection[i], collection[position] = collection[position], collection[i]

array = [3, 1, 5, 0, 7, 2, 5]
sorted_by_choice(array)
print(array)
