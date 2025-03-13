#include <iostream>
#include <vector>
using namespace std;

int N = 0;

void stack_Push(vector<int> &arr, int x)
{
    arr[N] = x;
    N++;
}

int stack_Pop(vector<int> &arr)
{
    if(N == 0) {return -1;}
    int temp = arr[N - 1];
    arr[N - 1] = 0;
    N--;
    return temp;

}
int stack_Count()
{
    return N;
}

int stack_IsEmpty()
{
    if(N == 0) {return 1;}
    else {return 0;}
}

int stack_Top(vector<int> arr)
{
    if(N == 0) {return -1;}
    return arr[N - 1];
}


int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int nn;
    cin >> nn;
    int order = 0;
    vector<int> arr(1000000);
    for(int i = 0; i < nn; i++)
    {
        cin >> order;
        switch (order)
        {
            case 1:
                cin >> order;
                stack_Push(arr, order);
                break;

            case 2:
                cout << stack_Pop(arr) << "\n";
                break;

            case 3:
                cout << stack_Count() << "\n";
                break;
            
            case 4:
                cout << stack_IsEmpty() << "\n";
                break;       

            case 5:
                cout << stack_Top(arr) << "\n";
                break;    
            default:
                break;
        }
    }
}