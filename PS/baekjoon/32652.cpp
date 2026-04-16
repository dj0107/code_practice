#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N;
    cin >> N;
    string aka = "AKARAKA"; 

    for(int i = 0; i < N - 1; i++)
    {
        aka += "RAKA";
    }

    cout << aka << endl;

}