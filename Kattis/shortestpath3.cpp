#include <bits/stdc++.h>
#define M 5000

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m, q, s;
    while (true) {

        cin >> n >> m >> q >> s;
        if (!(n | m | q | s)) break;

        vector<pair<int, int>> vs[M];

        int u, v, w;
        for (int i = 0; i < m; i++) {
            cin >> u >> v >> w;
            vs[u].push_back(make_pair(v, w));
        }

        int ds[M];
        for (int i = 0; i < n; i++) {
            ds[i] = INT32_MAX;
        }
        ds[s] = 0;

        for (int i = 0; i < n - 1; i++) {
            for (int u = 0; u < n; u++) {
                for (int j = 0; j < vs[u].size(); j++) {
                    int v = vs[u][j].first, w = vs[u][j].second;
                    if (ds[u] != INT32_MAX && ds[u] + w < ds[v])
                        ds[v] = ds[u] + w;
                }
            }
        }

        for (int i = 0; i < n - 1; i++) {
            for (int u = 0; u < n; u++) {
                for (int j = 0; j < vs[u].size(); j++) {
                    int v = vs[u][j].first, w = vs[u][j].second;
                    if (ds[u] == INT32_MIN)
                        ds[v] = INT32_MIN;
                    else if (ds[u] != INT32_MAX && ds[u] + w < ds[v])
                        ds[v] = INT32_MIN;
                }
            }
        }

        int t;
        for (int i = 0; i < q; i++) {
            cin >> t;
            if (ds[t] == INT32_MAX)
                cout << "Impossible" << endl;
            else if (ds[t] == INT32_MIN)
                cout << "-Infinity" << endl;
            else
                cout << ds[t] << endl;
        }

        cout << endl;

    }

    return 0;

}
