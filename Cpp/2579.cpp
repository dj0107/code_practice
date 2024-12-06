#include <iostream>
#include <vector>
using namespace std;



int main()
{
    int n;
    cin >> n;
    vector<vector<int>> maxScore(2); //maxScore[0]이 현재 계단을 밟았고 이전 계단에서 한 계단 올라온 경우, [1]이 두 계단 올라온 경우
    vector<int> score(n + 1);
    score[0] = 0;
    for(int i = 1; i <= n; i++)
    {
        cin >> score[i];
    }
    
    maxScore[0].push_back(0);
    maxScore[1].push_back(0);
    maxScore[0].push_back(score[1]);
    maxScore[1].push_back(score[1]);
    maxScore[0].push_back(score[1] + score[2]);
    maxScore[1].push_back(score[2]);

    for(int i = 3; i <= n; i++)
    {
        maxScore[0].push_back(maxScore[1][i - 1] + score[i]);
        maxScore[1].push_back(max(maxScore[0][i - 2], maxScore[1][i - 2]) + score[i]);
    }

    int totalScore = max(maxScore[0][n], maxScore[1][n]);

    cout << totalScore;
}