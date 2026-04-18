#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> totalCostR(n); // costX[Y] is total cost of painting first to Y-th house especially using X color at last house 
    vector<int> totalCostG(n);
    vector<int> totalCostB(n);

    vector<int> costR(n); // costs of painting each colors at each house
    vector<int> costG(n);
    vector<int> costB(n);

    for (int i = 0; i < n; i++)
    {
        cin >> costR[i] >> costG[i] >> costB[i];
    }

    totalCostR[0] = costR[0];
    totalCostG[0] = costG[0];
    totalCostB[0] = costB[0];


    for(int i = 1; i < n; i++)
    {
        totalCostR[i] = costR[i] + min(totalCostG[i - 1], totalCostB[i - 1]);
        totalCostG[i] = costG[i] + min(totalCostR[i - 1], totalCostB[i - 1]);
        totalCostB[i] = costB[i] + min(totalCostR[i - 1], totalCostG[i - 1]);
    }

    int minCost = min(min(totalCostR[n - 1], totalCostG[n - 1]), totalCostB[n - 1]);

    cout << minCost;
}