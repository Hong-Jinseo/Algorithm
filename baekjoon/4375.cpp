// 수학
// 1

#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	
	int n;
	
	while (cin >> n) {

		int answer = 1;
		int cnt = 1;

		while (true) {
			if (answer % n == 0) {
				break;
			} else {
				cnt++;
				answer = (answer * 10 + 1) % n;
			}
		}

		cout << cnt << endl;
	}

	return 0;
}