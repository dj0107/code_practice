#include <iostream>
#include <vector>
using namespace std;
const int MAX = 30;
int main()
{
    vector<vector<int>> combVec; //combVec[a][b] is aCb

    vector<int> hollowVec(1);
    hollowVec[0] = 0;
    combVec.push_back(hollowVec);

    for(int i = 1; i <= MAX; i++)
    {
        for(int j = 0; j <= i; j++)
        {
            hollowVec.push_back(0);
            combVec.push_back(hollowVec);
        }
    }


    //use pascal`s triangle law
    combVec[0][0] = 1;
    for(int i = 1; i <= MAX; i++)
    {
        combVec[i][0] = 1;
        combVec[i][i] = 1;
        for(int j = 1; j < i; j++)
        {
            int sum = 0;
            
            
            for(int k = 1; k <= i - j + 1; k++)
            {
                sum += combVec[i - k][j - 1];
            }

            combVec[i][j] = sum;
            
        }
    }
    int t;
    cin >> t;
    vector<int> ansVec(t);
    for(int i = 0; i < t; i++)
    {
        int n, m;   
        cin >> n >> m;
        ansVec[i] = combVec[m][n];
    }

    for(int i = 0; i < t; i++)
    {
        cout << ansVec[i] << "\n";
    }

}