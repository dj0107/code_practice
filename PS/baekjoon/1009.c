#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		int ans = 0;
		if (a % 10 == 1) ans = 1;
		else if (a % 10 == 2) {
			if (b % 4 == 0) ans = 6;
			else if (b % 4 == 1) ans = 2;
			else if (b % 4 == 2) ans = 4;
			else if (b % 4 == 3) ans = 8;
		}
		else if (a % 10 == 3) {
			if (b % 4 == 0) ans = 1;
			else if (b % 4 == 1) ans = 3;
			else if (b % 4 == 2) ans = 9;
			else if (b % 4 == 3) ans = 7;
		}
		else if (a % 10 == 4) {
			if (b % 2 == 0) ans = 6;
			else if (b % 2 == 1) ans = 4;
		}
		else if (a % 10 == 5) ans = 5;
		else if (a % 10 == 6) ans = 6;
		else if (a % 10 == 7) {
			if (b % 4 == 0) ans = 1;
			else if (b % 4 == 1) ans = 7;
			else if (b % 4 == 2) ans = 9;
			else if (b % 4 == 3) ans = 3;
		}
		else if (a % 10 == 8) {
			if (b % 4 == 0) ans = 6;
			else if (b % 4 == 1) ans = 8;
			else if (b % 4 == 2) ans = 4;
			else if (b % 4 == 3) ans = 2;
		}
		else if (a % 10 == 9) {
			if (b % 2 == 0) ans = 1;
			else if (b % 2 == 1) ans = 9;
		}
		else if (a % 10 == 0) ans = 10;

		printf("%d\n", ans);
	}
	
	return 0;
}