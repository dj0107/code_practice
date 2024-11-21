#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> vecAddition(vector<vector<int>> arr1, vector<vector<int>> arr2)
{
    vector<vector<int>> resultVec(arr1.capacity());
    for(int i = 0; i < arr1.capacity(); i++)
    {
        for(int j = 0; j < arr1[0].capacity(); j++)
        {
            resultVec[i].push_back(arr1[i][j] + arr2[i][j]);
        }
    }
    return resultVec;
}

int main()
{
    int N, M, temp;
    cin >> N >> M;

    vector<vector<int>> arr1(N), arr2(N);

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cin >> temp;
            arr1[i].push_back(temp);
        }
    }
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cin >> temp;
            arr2[i].push_back(temp);
        }
    }

    vector<vector<int>> ans = vecAddition(arr1, arr2);

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cout << ans[i][j];
            if(j < M - 1) {cout << " ";}
        }
        if(i < N - 1) {cout << "\n";}
    }

}