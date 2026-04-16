#include <stdio.h>
#include <stdlib.h>
int main() {

	int t; scanf("%d", &t);
	for (int i=0; i < t; i++) {
		int n; 
		scanf("%d", &n);
		int *c, *p;
		c = (int *)malloc(sizeof(int) * (n+1));
		p = (int *)malloc(sizeof(int) * (n+1));
		for (int j=1; j<=n; j++) scanf("%d%d", &c[j], &p[j]);
		float dp[100001]; //n->1
		for (int j=0; j<=n; j++) dp[j] = 0.0f;
		dp[n] = c[n];
		for (int j=n-1; j>=1; j--) {
			dp[j] = dp[j+1] > c[j] + dp[j+1] * (100 - p[j]) / 100.0f ? dp[j+1] : c[j] + dp[j+1] * (100 - p[j]) / 100.0f;
		}
		printf("%f\n", dp[1]);
		free(c); free(p);
	}

	return 0;
}