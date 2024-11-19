#include <iostream>
using namespace std;

int recursive_sum(int n) {
    if(n == 1) return 1;
    else if(n == 2) return 2;
    else if(n == 3) return 4;
    else {
        return recursive_sum(n - 1) + recursive_sum(n - 2) + recursive_sum(n - 3);
    }
}

int main() {

    int T;
    cin >> T;

    for(int i = 0; i < T; i++) {
        int n;
        cin >> n;
        cout << recursive_sum(n) << endl; 
    }

    return 0;
}