#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
long long mypow(long long a, long long b, long long n)
{
    if(b == 0) {return 1;}
    else if(b == 1){return a;}
    else if(b % 2 == 0)
    {
        long long mid = mypow(a, (b / 2), n);
        if(mid * mid >= n) {return n+1;}
        else
            return mid * mid;
    }
    else
    {
        long long mid = mypow(a, ((b - 1) / 2), n);
        if(a * mid * mid >= n) {return n+1;}
        else
            return a *mid * mid;
    }
}
int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    long long n, k;
    vector<long long> ansVec(t);
    for(int i = 0; i < t; i++)
    {
        cin >> n >> k;
        long long divs = (n / mypow(2, k, n));
        long long ans = (divs + 1) / 2;
        ansVec[i] = ans;
    }

    for(int i = 0; i < t; i++)
    {
        cout << ansVec[i] << "\n";
    }
}