// 수학
// 최대공약수와 최소공배수

#include <iostream>
using namespace std;

int gcd(int a, int b) {
	if (b == 0) {
		return a;
	}
	return gcd(b, a % b);
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, m;
	cin >> n >> m;

	// 최대공약수
	int ans1;
	if (n < m) {
		ans1 = gcd(n, m);
	}
	else {
		ans1 = gcd(m, n);
	}

	// 최소공배수
	int ans2 = ans1 * (n / ans1) * (m / ans1);

	cout << ans1 << "\n" << ans2;

	return 0;
}