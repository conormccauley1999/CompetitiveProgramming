// Problem 5

#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

int smallest(int n) {

	for (int i = 1;; i++) {

		for (int j = 1; j <= n; j++) {
			if (i % j != 0) break;
			if (j == n) return i;
		}

	}

	return 0;

}

int main() {
    
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		cout << smallest(n) << "\n";
	}

	return 0;

}
