// сортировка пузырьком на C#

void BubleSorted(int[] collection)
{
    for (int i = 1; i < collection.Length; i++)
    {
        for (int j =0; j < collection.Length; j++)
        {
            if(collection[i] < collection[j])
            {
                (collection[i], collection[j]) = (collection[j], collection[i]);
            }
        }
    }
}

int[] array = new int[]{3, 1, 4, 8, 5, 0, 3};
BubleSorted(array);
System.Console.WriteLine(string.Join(", ", array));