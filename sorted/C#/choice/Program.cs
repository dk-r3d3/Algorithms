// Сортировка выбором

void SortedByChoice(int[] collection)
{
    int size = collection.Length;
    for (int i = 0; i < size; i++)
    {
        int position = i;
        for (int j = i + 1; j < size; j++)
        {
            if (collection[j] < collection[position])
            {
                position = j;
            }
        }
        (collection[i], collection[position]) = (collection[position], collection[i]);
    }
}

int[] array = new int[]{3, 1, 4, 8, 5, 0, 3};
SortedByChoice(array);
System.Console.WriteLine(string.Join(", ", array));