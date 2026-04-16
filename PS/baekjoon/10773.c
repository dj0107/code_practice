#include <stdio.h>
#include <stdlib.h>

int main() {
	int k;
	scanf("%d", &k);
	int *stk;
	stk = (int *)malloc(sizeof(int) * k);
	int cnt = 0;
	for (int i=0; i<k; i++) {
		int l;
		scanf("%d", &l);
		if (l != 0) {
			stk[cnt] = l;
			cnt++;
		}
		else {
			stk[cnt] = 0;
			cnt--;
		}

	}
	int total = 0;
	for (int i=0; i<cnt; i++) {
		total += stk[i];
	}
	printf("%d\n", total);
	free(stk);
}