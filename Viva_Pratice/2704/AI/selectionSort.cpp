#include <iostream>

using namespace std;

void swap(int *a, int *b)
{
    (*a) = (*a) + (*b);
    (*b) = (*a) - (*b);
    (*a) = (*a) - (*b);
}

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
}

void selectionSort(int arr[], int n)
{
    int mindInd, j;
    for (int i = 0; i < n - 1; i++)
    {
        mindInd = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[mindInd])
            {
                mindInd = j;
            }
        }
        swap(arr[i], arr[mindInd]);
    }
}

int main()
{
    int arr[] = {20, 10, 40, 60, 80};
    int n = 5;
    selectionSort(arr, n);
    printArray(arr, n);
    return 0;
}