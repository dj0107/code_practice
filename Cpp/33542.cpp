#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

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

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int a, b; // score of Donghyeon and Juwon 
    cin >> a >> b;
    int n; // number of targets
    cin >> n;
    vector<int> lefty(n + 1); // score if hit the target with left ball
    vector<int> righty(n + 1); // score if hit the target with right ball
    righty[0] = 0;
    for(int i = 1; i <= n; i++)
    {
        cin >> lefty[i] >> righty[i];
    }
    // input part over

    // set minimum
    int min = a - b;

    // sort righty vector
    vector<int> rightySorted = righty;
    sort(rightySorted.begin(), rightySorted.end());

    // calculate for each lefty score and store target number
    int leftNum = 0;
    int rightNum = 0;
    int finalMin = 2147483647;


    for(int i = 1; i <= n; i++)
    {
        int newMinRequired = min - lefty[i];
        int newRightNum = binaryCloseSearch(rightySorted, newMinRequired + 1);
        auto k = find(righty.begin(), righty.end(), rightySorted[newRightNum]);
        int tempRightNum = distance(righty.begin(), k);
        if(tempRightNum == i)
        {
            if(newRightNum < n) 
            {
            newRightNum++;
            k = find(righty.begin(), righty.end(), rightySorted[newRightNum]);
            tempRightNum = distance(righty.begin(), k);
            }
            else {newRightNum = -1;}
        }
        if(newRightNum != -1 && (lefty[i] + rightySorted[newRightNum] < finalMin))
        {
            leftNum = i;
            rightNum = tempRightNum;
            finalMin = lefty[i] + rightySorted[newRightNum];
        }

    }


    if(a <= b) {cout << "-1 -1";}
    else if(finalMin == 2147483647) {cout << "No";}
    else
    {
        cout << leftNum << " " << rightNum;
    }

    


}