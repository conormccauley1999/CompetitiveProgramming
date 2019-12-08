#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int n, d;
	cin >> n;
	d = (n == 1) ? 1 : ceil(log2((double) n)) + 1;
	cout << d << endl;
}
