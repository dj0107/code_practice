#include <iostream>
using namespace std;


int main() {
    int n;
    cin >> n;

    int N1 = 1;
    int N2 = 2;

    if(n == 1) cout << 1 << endl;
    else if (n == 2) cout << 2 << endl;

    else {
        for(int i=0; i<n-2; i++) {
            if(i % 2 == 1) {
                N2 = (N1 + N2) % 10007;
            }
            else{
                N1 = (N1 + N2) % 10007;
            }
        }
        if(n % 2 == 1) cout << N1 % 10007 << endl;
        else cout << N2 % 10007 << endl;
    }



    return 0;
}