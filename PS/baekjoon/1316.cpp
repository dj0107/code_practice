// SOLVED
#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;
	int answer = n; // 연속 아닌 단어마다 1씩 깎기
	for (int i = 0; i < n; i++) {
		string word;
		cin >> word;
		char latest = '0';
		for (int j = 0; j < word.size(); j++) {
			if (word[j] != latest) {
				// 이전에 같은단어 있었나 확인하기
				bool overlap = false;
				for (int k = 0; k < j; k++) {
					if (word[j] == word[k]) {
						overlap = true;
						break;
					}
				}
				if (overlap) {
					answer--;
					break;
				}
				latest = word[j];
			}
		}
	}
	cout << answer;
}