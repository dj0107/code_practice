#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, m;
	int best6, best;
	best6 = 1001; best = 1001;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++) {
		int price6, price;
		scanf("%d%d", &price6, &price);
		if (price6 < best6) best6 = price6;
		best = price < best ? price : best;

	}
	int total = 0;
	if (best6 > best * 6) total = best * n;
	else {
		// buy 6 bunch first
		int mok = n / 6;
		total += mok * best6;
		n -= mok * 6;
		total += n * best < best6 ? n * best : best6;

	}
	printf("%d\n", total);
}