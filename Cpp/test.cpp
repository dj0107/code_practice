#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
long long mypow(long long a, long long b)
{
    if(b == 0) {return 1;}
    else if(b == 1){return a;}
    else if(b % 2 == 0)
    {
        long long mid = mypow(a, (b / 2));
        return mid * mid;
    }
    else
    {
        long long mid = mypow(a, (b / 2));
        return a * mid * mid;
    }
}
int binaryCloseSearch(vector<int> arr, int target)
{
    int start = 0;
    int end = arr.size() - 1;
    int mid = (start + end) / 2;
    while(start < end)
    {
        mid = (start + end) / 2;
        if(arr[mid] == target) {return mid;}
        else if(arr[mid] > target)
        {
            if(arr[mid - 1] <= target) {return mid;}
            end = mid - 1;
        }
        else if(arr[mid] < target)
        {
            if(arr[mid + 1] >= target) {return mid + 1;}
            start = mid + 1;
        }
    }
    if(arr[mid] > target) {return 0;}
    else if(arr[mid] < target) {return -1;}
}

int main() {
    //vector<int> arr = {2,4,6,8,10,12,14,16};
    //cout << binaryCloseSearch(arr, -1);
    long long a, b;
    a = 3;
    b = 5;
    cout << mypow(a, b);
}