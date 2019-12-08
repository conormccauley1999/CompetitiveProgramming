#include <bits/stdc++.h>
using namespace std;

int main() {

	int n;
	cin >> n;

	vector<int> T(n);
	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		T.push_back(t);
	}
	sort(T.begin(), T.end(), greater<int>());

	int mxt = 0;
	int mxi = 0;
	for (int i = 0; i < n; i++) {
		if (T[i] - (n - i) >= mxt) {
			mxt = T[i] - (n - i);
			mxi = i;
		}
	}

	cout << T[mxi] + mxi + 2 << endl;

}
