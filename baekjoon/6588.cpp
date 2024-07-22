// 수학
// 골드바흐의 추측

#include <iostream>
#include <cmath>
#define SIZE 1000001
using namespace std;

bool primeNum[SIZE];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	// 소수 찾기
	fill_n(primeNum, SIZE, true);
	primeNum[0] = false;
	primeNum[1] = false;

	for (int i = 2; i < sqrt(SIZE); i++) {
		if (primeNum[i]) {
			for (int j = i * 2; j < SIZE; j += i) {
				primeNum[j] = false;
			}
		}
	}

	int n;
	cin >> n;

	while (n != 0) {
		for (int idx = 0; idx < n/2 + 1; idx++) {
			if (primeNum[idx] && primeNum[n - idx]) {
				cout << n << " = " << idx << " + " << n - idx << "\n";
				break;
			}
		}
		cin >> n;
	}

	return 0;
}