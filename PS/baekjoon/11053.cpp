#include <iostream>
using namespace std;

int main()
{
    int arr[1001];
    int n;
    cin >> n;


    for(int i = 1; i <= n; i++)
    {
        cin >> arr[i];
    }

    int dp[1001];
    
    dp[0] = 0;
    dp[1] = 1;

    for(int i = 2; i <= n; i++)
    {
        dp[i] = 1;
        for(int j = 1; j < i; j++)
        {
            if(arr[i] > arr[j])
            {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    int maximun = dp[1];
    for(int i = 2; i <= n; i++)
    {
        maximun = max(maximun, dp[i]);
    }

    cout << maximun << endl;
}