// Problem 4

#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

bool palindrome(int n) {
	if (n % 10           != (n % 1000000) / 100000) return false;
	if ((n % 100) / 10   != (n % 100000) / 10000) 	return false;
	if ((n % 1000) / 100 != (n % 10000) / 1000) 	return false;
	return true;
}

int smallest(int n) {

	for (int j = n - 1; j > 10000; j--) {

		if (!palindrome(j)) continue;

		for (int k = 100; k < 1000; k++) {
			if (j % k == 0 && j / k >= 100 && j / k < 1000) return j;
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
