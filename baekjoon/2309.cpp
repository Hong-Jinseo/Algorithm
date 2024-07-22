// 브루트 포스
// 일곱 난쟁이

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int arr[9];
	int total = 0;

	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
		total += arr[i];
	}

	sort(arr, arr + 9);

	for (int i = 0; i < 8; i++) {
		for (int j = i + 1; j < 9; j++) {
			if ((total - arr[i] - arr[j]) == 100) {
				arr[i] = -1;
				arr[j] = -1;
				break;
			}
		}
		if (arr[i] == -1) {
			break;
		}
	}

	for (int i = 0; i < 9; i++) {
		if (arr[i] > 0) {
			cout << arr[i] << endl;
		}
	}

	return 0;
}