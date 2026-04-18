#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int ki(int a[][3]) {
    return a[0][2];
}

int main() {
	srand(15578884844);
    float *a = new float[100]; // 10x10 행렬
    float *b = new float[100];
    float *c = new float[100];
    for(int i = 0; i < 100; i++) {
        a[i] = 2.13f * i; b[i] = 1.24f *i; c[i] = 0;
    }
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                c[i*10+j] += a[i*10+k] * b[k*10+j];
            }
        }
    }
    float *v = new float[10];
    float *buf = new float[10];
    float *final1 = new float[10];
    float *final2 = new float[10];
	for (int i = 0; i < 10; i++) 
	{
		v[i] = float(rand() % 2); 
        buf[i] = 0; final1[i] = 0; 
        final2[i] = 0;
	}
    
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            // Bv
            buf[i] += b[i*10+j] * v[j];
    
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            // A (Bv) 
            final1[i] += a[i*10+j] * buf[j];
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            // Cv
            final2[i] += c[i*10+j] * v[j];
    
    for (int i = 0; i < 10; i++) cout << final1[i] << " AND " << final2[i] << endl;

}