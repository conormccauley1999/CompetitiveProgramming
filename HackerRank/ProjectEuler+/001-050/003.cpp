// Problem 3

#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

int main() {
    
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {

		ull n;
		cin >> n;

		for (ull j = 2; (j * j) <= n; j++) {
			while (n % j == 0 && n != j) n /= j;
		}

		cout << n << "\n";

	}

	return 0;

}
