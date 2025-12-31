#include <iostream>
using namespace std;

int binarySearch(int target, int arr[], int size)
{
    int start = 0;
    int end = size - 1;

    while(start < end)
    {
        int mid = (start + end) / 2;
        if(arr[mid] == target)
            return mid;
        else if(arr[mid] > target)
            end = mid;
        else
            start = mid + 1;
    }
    return -1;
}

int main()
{
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    cout << binarySearch(4, arr, 10) << endl;
}