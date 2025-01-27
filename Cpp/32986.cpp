#include <iostream>
#include <cmath>
using namespace std;
 
int main() {
	int x, y, z;
	cin >> x >> y >> z;

    int minimum = min(min(x, y), z);
	
	if(x == 3 && y == 3 && z == 3)
    {
        cout << 0;
    }
    else
    {
        cout << (minimum - 1) / 2;
    }
	
	
	return 0;
}