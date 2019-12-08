#include <iostream>

using namespace std;

const int m = 50000000;

int main() {

	bool* ps = new bool[m + 1];
	ps[0] = false;
	ps[1] = false;
	int i = 2;
	while (i <= m) ps[i++] = true;
	i = 2;
	while (i * i <= m) {
		if (ps[i]) {
			int j = i * i;
			while (j <= m) {
				ps[j] = false;
				j += i;
			}
		}
		i++;
	}

	int x;
	cin >> x;

	int k = 0;
	int d = 2;

	for (int a = 2; a < m; a++) {
		if (!ps[a]) continue;
		if (x == 1) break;
		while (x % a == 0) {
			x /= a;
			k++;
		}
	}

	if (k == 0) k = 1;

	cout << k << endl;

}
