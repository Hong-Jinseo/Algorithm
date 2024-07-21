// 수학
// 약수

#include <iostream>
#include <algorithm>
using namespace std;

int arr[51];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int cnt;
	cin >> cnt;

	for (int i = 0; i < cnt; i++) {
		cin >> arr[i];
	}

	sort(arr, arr + cnt);
	int ans = arr[0] * arr[cnt - 1];

	cout << ans;

	return 0;
}