#include <stdio.h>
#include <stdlib.h>

int main() {
	int n;
	int total = 0;
	scanf("%d", &n);
	int *A, *B;
	A = (int*)malloc(sizeof(int) * n);
	B = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++) scanf("%d", &A[i]);
	for (int i = 0; i < n; i++) scanf("%d", &B[i]);

	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++) {
			if (A[i] > A[j]) {
				int tmp = A[i];
				A[i] = A[j];
				A[j] = tmp;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		// find min of B
		int max = -1;
		int idx = 0;
		for (int j=0; j<n; j++) {
			if (B[j] > max) {
				idx = j;
				max = B[idx];
			}
		}
		total += A[i] * max;
		B[idx] = -1;
	}
	printf("%d\n", total);



	free(A); free(B); 
}