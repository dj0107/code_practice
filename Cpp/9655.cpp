#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    if(N % 4 == 1 || N % 4 == 3)
    {
        cout << "SK";
    }
    else 
    {
        cout << "CY";
    }
}