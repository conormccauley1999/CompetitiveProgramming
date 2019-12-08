#include <iostream>
using namespace std;

int main() {

	while (true) {

		int n;
		cin >> n;
		if (n == -1) break;

		int a[n][n];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				cin >> a[i][j];
		
		int r[n];
		for (int i = 0; i < n; i++) r[i] = 0;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				for (int k = j + 1; k < n; k++)
					r[i] |= (a[i][j] & a[i][k] & a[j][k]);
		
		for (int i = 0; i < n; i++)
			if (!r[i]) cout << i << " ";

		cout << endl;

	}

}
