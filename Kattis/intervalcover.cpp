#include <bits/stdc++.h>
#define N 20000

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    double A, B;
    while (cin >> A >> B) {

        int n;
        double a, b;
        vector<pair<double, double>> vs;

        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a >> b;
            vs.push_back(make_pair(a, b));
        }

        bitset<N> used;
        double cur = A;
        bool poss = true;

        do {

            double mx = cur;
            int mxi = 0;
            bool any = false;

            for (int i = 0; i < n; i++) {
                if (!used[i] && vs[i].first <= cur && vs[i].second >= mx) {
                    mx = vs[i].second;
                    mxi = i;
                    any = true;
                }
            }

            if (!any) {
                poss = false;
                break;
            }
            
            used[mxi] = 1;
            cur = mx;

        } while (cur < B);

        if (poss) {
            cout << used.count() << endl;
            for (int i = 0; i < n; i++) {
                if (used.test(i)) cout << i << " ";
            }
            cout << endl;
        } else {
            cout << "impossible" << endl;
        }

    }

    return 0;

}
