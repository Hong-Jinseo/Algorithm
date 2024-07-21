// 수학
// 소수 찾기

#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, tmp, answer = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> tmp;
		bool ret = true;

		for (int j = 2; j < tmp; j++) {
			if (tmp % j == 0) {
				// 소수가 아님
				ret = false;
				break;
			}
		}

		if (ret && tmp != 1) {
			answer += 1;
		}
	}

	cout << answer;

	return 0;
}