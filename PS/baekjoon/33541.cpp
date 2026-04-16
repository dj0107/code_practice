#include <iostream>
using namespace std;

int main()
{
    int x;
    cin >> x;
    x++;
    while(x < 10000)
    {
        int front = x / 100;
        int end = x % 100;
        if((front + end) * (front + end) == x)
        {
            cout << x;
            break;
        }
        x++;
    }
    if(x == 10000) {cout << -1;}
}