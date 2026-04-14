#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		char str[51];
		scanf("%s", &str);
		char stk[50];
		int top = -1;
		int valid = 1;
		for (int j = 0; j < 50; j++) {
			if (str[j] == '\0') break;
			else if (str[j] == '(')
			{
				top += 1;
				stk[top] = str[j];
			}
			else {
				if (top == -1) {
					valid = 0;
					break;
				}
				else {
					stk[top] = '\0';
					top -= 1;
				}
			}
		}
		if (valid == 0 || top != -1) printf("NO\n");
		else printf("YES\n");
	}

	return 0;
}