#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
	int t; scanf("%d", &t);
	for(int tc=0; tc<t; tc++) {
		int n; scanf("%d", &n);
		int arr[5001];
		for (int i=1; i<=n; i++) scanf("%d", &arr[i]);

		for (int i=1; i<=n; i++) {
			int low = 0; int high = 0;
			for (int j=i+1; j <= n; j++) {
				if (arr[j] > arr[i]) high++;
				else if (arr[j] < arr[i]) low++;
			}
			arr[i] = low > high ? low : high;

		}
		for (int i=1; i<n; i++) printf("%d ", arr[i]);
		printf("%d\n", arr[n]);
	}
}