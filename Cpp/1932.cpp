#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<vector<int>> dp;
    int n;
    cin >> n;
    vector<int> hollowVec(n);

    for(int i = 0; i < n; i++)
    {
        hollowVec[i] = 0;
    }

    for(int i = 0; i < n; i++)
    {
        dp.push_back(hollowVec);
    }
    cin >> dp[0][0];

    vector<int> nums(n); //get input


    for(int i = 1; i < n; i++)
    {
        for(int j = 0; j <= i; j++)
        {
            cin >> nums[j];
            if(j > 0)
            {
                dp[i][j] = max(dp[i - 1][j - 1] + nums[j], dp[i][j]);
            }
            if(j < i)
            {
                dp[i][j] = max(dp[i - 1][j] + nums[j], dp[i][j]);
            }
        }
    }

    int ans = *max_element(dp[n - 1].begin(), dp[n - 1].end());

    cout << ans << endl;

}