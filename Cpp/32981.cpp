#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int q, n;
    cin >> q;
    vector<int> resultarr(10000000);
    long long result = 4;
    resultarr[0] = 5;
    for(int i = 1; i < 10000000; i++)
    {
        result *= 5;
        result %= 1000000007;
        
        resultarr[i] = static_cast<int>(result);
    }

    vector<int> ns(q);

    for(int i = 0; i < q; i++)
    {
        cin >> n;
        ns[i] = n;
    }

    for(int i = 0; i < q; i++)
    {
        cout << resultarr[ns[i] - 1] << "\n"; 
    }

    
}