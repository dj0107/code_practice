#include <iostream>
#include <vector>
using namespace std;

int main()
{
    long long dp[101];
    dp[0] = 0; dp[1] = 1; dp[2] = 1; 
    dp[3] = 1; dp[4] = 2; dp[5] = 2;

    for(int i = 6; i <= 100; i++)
    {
        dp[i] = dp[i - 1] + dp[i - 5];
    }

    int t;
    cin >> t;
    vector<long long> arrVec(t);
    for(int i = 0; i < t; i++)
    {
        cin >> arrVec[i];
    }

    for(int i = 0; i < t; i++)
    {
        cout << dp[arrVec[i]] << "\n";
    }
    
}