// 수학
// 약수의 합

#include <iostream>
#define MAX 1000001
using namespace std;

long long dp[MAX];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	for (int i = 1; i < MAX; i++) {
		for (int j = i; j < MAX; j += i) {
			dp[j] += i;
		}
		dp[i] += dp[i - 1];		// g(x)를 만들어주는 부분
	}

	int T;
	cin >> T;

	for (int t = 0; t < T; t++) {
		int n;
		cin >> n;
		cout << dp[n] << "\n";
	}

	return 0;
}