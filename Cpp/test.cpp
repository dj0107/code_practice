#include <iostream>
#include <cmath>
#include <random>


inline void init_vec(float *a, int N) {
        /****************/
        /* TODO: put your own parallelized code here */
        /* You don't have to parallelize all of your code - it's up to you. */

        srand(0);
        for (int i = 0; i < N; i++) {
                a[i] = (float)(rand() % 2);
                std::cout << a[i] << std::endl;
        }
        
        /****************/
}

int main() {
    float *a = new float[200];
    init_vec(a, 200);

    return 0;
}