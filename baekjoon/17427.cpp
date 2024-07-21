// 수학
// 약수의 합 2

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	long long answer = 0;	// int 안 됨

	for (int i = 1; i <= n; i++) {
		// 약수의 합 += (n보다 작거나 같은 i의 배수의 개수) * i
		answer += (n / i) * i;
	}

	cout << answer;

	return 0;
}