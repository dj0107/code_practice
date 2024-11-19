#include <iostream>
using namespace std;

int sugar(int N) {
    if(N>5) {
        int tmp = sugar(N-5);
        if (tmp == -1) {
            if(N % 3 == 0) {
                return N/3;
            }
            else{
                return -1;
            } 
        }
        else {
            return tmp + 1 ;
        }
    }
    else if (N == 3 or N == 5) {
        return 1;
    }
    else if (N == 1 or N == 2 or N == 4) {
        return -1; //3이나 5로 안된다는 뜻
    }
}

int main() {
    
    int N;
    cin >> N;

    cout << sugar(N) << endl;

    return 0;
}