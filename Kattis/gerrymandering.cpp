#include <bits/stdc++.h>
#define vpi vector< pair<int, int> >
#define pi pair<int, int>
#define pb push_back
#define mp make_pair
#define f first
#define s second
using namespace std;

int main() {

	int p, d;
	cin >> p >> d;

	vpi ds(d);

	for (int i = 0; i < d; i++)
		ds.pb(mp(0, 0));
	
	for (int i = 0; i < p; i++) {
		int di, a, b;
		cin >> di >> a >> b;
		ds[di - 1].f += a;
		ds[di - 1].s += b;
	}

	int tv = 0;
	int wa = 0;
	int wb = 0;

	for (int i = 0; i < d; i++) {
		pi v = ds[i];
		cout << (v.f > v.s ? "A " : "B ");
		tv += (v.f + v.s);
		int wai, wbi;
		wai = (v.f > v.s ? v.f - (((v.f + v.s) / 2) + 1) : v.f);
		wbi = (v.s > v.f ? v.s - (((v.f + v.s) / 2) + 1) : v.s);
		wa += wai;
		wb += wbi;
		cout << wai << " " << wbi << endl;
	}

	printf("%.6f\n", abs(wa - wb) / (tv + 0.0));

}
