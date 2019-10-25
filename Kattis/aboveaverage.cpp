#include <bits/stdc++.h>
using namespace std;

int main() {

	int c;
	cin >> c;	
	while (c--) {

		int n;
		cin >> n;
		int g[n];
		double t = 0;
		for (int i = 0; i < n; i++) {
			cin >> g[i];
			t += g[i];
		}
		t /= (double) n;
		int r = 0;
		for (int i = 0; i < n; i++)
			if (g[i] > t) r++;
		r *= 100;
		printf("%.3f%%\n", r / (double) n);

	}

}
