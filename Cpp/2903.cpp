#include <iostream>
#include <cmath>
using namespace std;

long long mypow(long long a, long long b)
{
    long long ans = 1;
    for(long long i = 0; i < b; i++)
    {
        ans *= a;
    }
    return ans;
}

int main()
{   

    //단계를 진행할 때마다 변이 2등분이 됨.
    long long N;
    cin >> N;
    cout << mypow(mypow(2,N) + 1,2) << endl;
}