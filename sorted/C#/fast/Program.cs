// Быстрая сортировка

int FindPivot(int[] collection, int minIndex, int maxIndex) // находим опорный элемент
{
    int pivot = minIndex - 1; // опорный элемент крайний справа
    int temp = 0;
    for (int i = minIndex; i < maxIndex; i++) // далее минИндекс = 0
    {
        if (collection[i] < collection[maxIndex])
        {
            pivot++;
            temp = collection[pivot];
            collection[pivot] = collection[i];
            collection[i] = temp;
        }
    }
    pivot++;
    (collection[maxIndex], collection[pivot]) =(collection[pivot], collection[maxIndex]);
    return pivot;
}

int[] QuickSort(int[] collection, int minIndex, int  maxIndex) // возвращает числовой массив
{
    if (minIndex >= maxIndex)
    {
        return collection;
    }
    int pivot = FindPivot(collection, minIndex, maxIndex); // получаем индекс опорного для дальнейшего вызова той же самой функции
    QuickSort(collection, minIndex, pivot - 1);
    QuickSort(collection, pivot + 1, maxIndex);
    return collection;
}

void Main(int[] collection)
{
    collection = QuickSort(collection, 0, collection.Length - 1);
}
int[] array = new int[]{6, 1, 3, 8, 5, 0, 3};
Main(array);
System.Console.WriteLine(string.Join(", ", array));