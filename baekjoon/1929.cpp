// 수학
// 소수 찾기

#include <iostream>
#include <algorithm>
#include <cmath>
#define SIZE 1000001
using namespace std;
bool arr[SIZE];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	fill_n(arr, SIZE, true);	// true:소수, false:소수아님
	arr[0] = false;
	arr[1] = false;

	// 에라토스테네스의 체
	for (int i = 2; i < SIZE; i++) {
		if (arr[i]) {
			for (int j = i * 2; j < SIZE; j += i) {
				arr[j] = false;
			}
		}
	}

	int m, n;
	cin >> m >> n;

	for (int i = m; i <= n; i++) {
		if (arr[i]) {
			cout << i << "\n";
		}
	}
    
	return 0;
}