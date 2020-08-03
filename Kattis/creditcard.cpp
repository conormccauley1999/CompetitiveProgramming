#include <bits/stdc++.h>

using namespace std;

double rnd(double x) {
    return (int) (x * 100.0 + 0.50000001) / 100.0;
}

int sol(double r, double b, double m) {

    for (int p = 1; p <= 1200; p++) {

        double c = b;
        b = rnd(b * r) - m;

        if (b <= 0)
            return p;
        else if (b >= c) {
            return 1201;
        }

    }

    return 1201;

}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while (t--) {

        double r, b, m;
        cin >> r >> b >> m;

        r = 1.0 + (r / 100.0);
    
        int x = sol(r, b, m);

        if (x <= 1200)
            cout << x << endl;
        else
            cout << "impossible" << endl;

    }

    return 0;

}
