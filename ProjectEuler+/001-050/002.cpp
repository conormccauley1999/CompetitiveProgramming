// Problem 2

#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

int main() {
    
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {

		ull n;
		cin >> n;

		ull sm = 0;

		ull a, b;
		a = 1;
		b = 1;

		while (a <= n) {

			if (a % 2 == 0) sm += a;

			ull t = a + b;
			b = a;
			a = t;

		}

		cout << sm << "\n";

	}

	return 0;

}
