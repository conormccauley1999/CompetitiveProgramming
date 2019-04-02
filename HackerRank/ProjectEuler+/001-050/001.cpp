// Problem 1

#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

ull sum(ull n) {
	return (n * (n + 1)) / 2;
}

int main() {
    
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {

		ull n;
		cin >> n;

		n--;

		cout << ((3 * sum(n / 3)) + (5 * sum(n / 5)) - (15 * sum(n / 15))) << "\n";

	}

	return 0;

}
