#include <iostream>
#include <vector>
using namespace std;

bool isUnder(vector<int> arr, int x)
{
    long long sum = 0;
    for(int i = 0; i < arr.size(); i++)
    {
        sum += max(0, arr[i] - x);
    }

    return sum <= x;

}

int main()
{
    int n;
    int maxDate = 0;
    cin >> n;
    vector<int> A(n), B(n);
    for(int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    for(int i = 0; i < n; i++)
    {
        cin >> B[i];
        A[i] = ((A[i] - 1) / B[i]) + 1; //use A as day vector to remove all leaves
        maxDate = max(maxDate, A[i]);
    }

    int start = 1;
    int end = maxDate;
    int mid;

    while(start <= end)
    {
        mid = (start + end) / 2;
        if(isUnder(A, mid) == true)
        {
            end = mid;
        }
        else
        {
            start = mid;
        }

        if(start + 1 >= end) {break;}
    }

    if(isUnder(A,start + 1))
    {
        start++;
    }

    cout << start << endl;

}