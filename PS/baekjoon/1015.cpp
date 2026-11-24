// 해결 완료
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int *arr = new int[n];
	int *answer = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	// copy array
	int *original = new int[n];
	for (int i = 0; i < n; i++) {
		original[i] = arr[i];
	}
	// sort array
	sort(arr, arr + n);

	for (int i = 0; i < n; i++) {
		// 자기 이전에 같은 값 있나 확인하기
		int same = 0;
		for (int j = 0; j < i; j++) {
			if (original[i] == original[j]) same++;
		}
		// 이렇게 구한 same이 가산됨

		// 정렬된 array에서 맞는 인덱스 찾기
		int pos = 0;
		for (int j = 0; j < n; j++) {
			if (arr[j] == original[i]) {
				pos = j;
				break;
			}
		}
		pos += same; // same 가산하기
		// 최종 정답 행렬에 넣기
		answer[i] = pos;
	}
	// answer 출력하기
	for (int i = 0; i < n - 1; i++) {
		cout << answer[i] << " ";
	}
	cout << answer[n - 1];

	delete []arr; delete []original; delete []answer;
}