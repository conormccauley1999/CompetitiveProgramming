#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, t;
    cin >> n >> t;

    vector<pair<int, int>> vs;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        vs.push_back(make_pair(a, b));
    }

    sort(vs.begin(), vs.end(), [](const pair<int, int>& x, const pair<int, int>& y) {
        if (x.first != y.first)
            return x.first > y.first;
        return x.second < y.second;
    });

    vector<int> q(t, 0);
    for (int i = 0; i < n; i++) {
        int j = vs[i].second;
        while (q[j] && j >= 0) j--;
        if (j >= 0) q[j] = vs[i].first;
    }

    int m = 0;
    for (int i = 0; i < t; i++) {
        m += q[i];
    }
    cout << m << endl;

    return 0;

}
