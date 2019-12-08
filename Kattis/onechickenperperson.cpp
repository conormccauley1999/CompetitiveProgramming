#include <iostream>
#include <string>
using namespace std;

int main() {

	int n, m;
	cin >> n >> m;

	string p;
	if (n > m) p = (n == m + 1) ? " piece" : " pieces";
	else p = (m == n + 1) ? " piece" : " pieces";

	if (n > m) cout << "Dr. Chaz needs " << n - m << " more" << p << " of chicken!" << endl;
	else cout << "Dr. Chaz will have " << m - n << p << " of chicken left over!" << endl;

}
