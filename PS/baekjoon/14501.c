#include <stdio.h>
#include <stdlib.h>

int main() {

	int N; scanf("%d", &N);
	int *T, *P, *dp;
	T = (int*)malloc(sizeof(int) * (N+1));
	P = (int*)malloc(sizeof(int) * (N+1));
	dp = (int*)malloc(sizeof(int) * (N+2));
	dp[0] = 0;
	for (int i=1; i<=N; i++) {
		scanf("%d%d", &T[i], &P[i]);
		dp[i] = 0; // total money at start of i day
	}
	
	for (int i=1; i<=N; i++) {
		dp[i] = dp[i] < dp[i-1] ? dp[i-1] : dp[i];
		if (i + T[i] <= N+1 && dp[i + T[i]] < dp[i] + P[i]) dp[i + T[i]] = dp[i] + P[i];
	}
	
	dp[N+1] = dp[N+1] < dp[N] ? dp[N] : dp[N+1];
	printf("%d\n", dp[N+1]);
	
	

	free(P); free(T); free(dp);
	return 0;
}