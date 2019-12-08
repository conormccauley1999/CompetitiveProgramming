#include <bits/stdc++.h>
#define vpi vector< pair<int, int> >
#define vi vector<int>
#define pi pair<int, int>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define fori(i,n) for(int i=0;i<(n);i++)
using namespace std;

void sieve(bool ps[], int n) {
	fill_n(ps, n, true);
	ps[0] = false;
	ps[1] = false;
	for (int i = 2; i * i <= n; i++)
		if (ps[i])
			for (int j = i * i; j <= n; j += i)
				ps[j] = false;
}

pi solve(bool ps[], int n) {
	fori(i, n)
		if (ps[i] && n % i == 0)
			return mp(i, n / i);
	return mp(0, 0);
}

int main() {

	int m = 1000000;
	bool ps[m];
	sieve(ps, m);

	int t;
	cin >> t;

	fori(i, t) {

		int n, e;
		cin >> n >> e;

		pi r = solve(ps, n);
		int x = (r.f - 1) * (r.s - 1);
		
		long d = 0;
		while (((++d) * e) % x != 1) { }
		
		cout << d << endl;

	}

}
