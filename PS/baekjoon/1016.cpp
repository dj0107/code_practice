// 풀이 성공
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	long long low, high;
	cin >> low >> high;
	int cnt = 0;
	vector<int> candidate(1000001); // 후보들
	candidate[0] = 1; candidate[1] = 1; // 제외
	// 0이면 소수, 1이면 소수가 아니라는 뜻.
	// 소수를 에라스토테네스 채로 구하고 그 제곱을 저장
	for (int i = 2; i <= 1000000; i++) {
		if (candidate[i] == 0) { // 소수
			// 배수들 모조리 1로 마킹
			for (int j = i * 2; j <= 1000000; j += i) {
				candidate[j] = 1;
			}
		}

	}
	// candidate[n] = 0 인 애들만 그 제곱을 prime으로 넣기
	vector<long long> prime_square;
	for (int i = 2; i <= 1000000; i++) {
		if (candidate[i] == 0) {
			prime_square.push_back((long long)i * i);
		}
	}
	
	int num_primes = prime_square.size();
	vector<int> final_vec(high - low + 1); // 마찬가지로 0이면 제곱 ㄴㄴ수, 1이면 아님, 인덱스가 min 만큼 보정된 배열임
	for (int i = 0; i < num_primes; i++) {
		// 최초 시작점 구하기
		long long sq = prime_square[i];
		long long start = (low / sq) * sq;
		if (low % sq != 0) {
			start += sq;
		}
		// sq 단위로 나아가며 똑같이 에라스토테네스 채 수행
		for (long long num = start; num <= high; num += sq) {
			final_vec[num - low] = 1;
		}

	}
	// 이제 final_vec 벡터에서 0인 원소들만 세면 끝
	for (int i = 0; i < final_vec.size(); i++) {
		if (final_vec[i] == 0) cnt++;
	}
	cout << cnt;

}