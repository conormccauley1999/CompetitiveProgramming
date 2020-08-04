#include <bits/stdc++.h>
#define M 10000

using namespace std;

bool bfs(vector<vector<int>> &a, vector<vector<int>> &e, int par[], int s, int t) {

    vector<bool> vis(e.size(), false);
    queue<int> q;

    q.push(s);
    vis[s] = true;
    par[s] = -1;

    while (!q.empty()) {

        int u = q.front();
        q.pop();

        for (int i = 0; i < a[u].size(); i++) {
            int v = a[u][i];
            if (!vis[v] && e[u][v] > 0) {
                q.push(v);
                par[v] = u;
                vis[v] = true;
                if (v == t) return true;
            }
        }

    }

    return vis[t];

}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m, s, t;
    cin >> n >> m >> s >> t;

    vector<vector<int>> a;
    vector<vector<int>> r;
    vector<vector<int>> e;

    for (int i = 0; i < n; i++) {
        a.push_back(vector<int>());
        r.push_back(vector<int>());
        e.push_back(vector<int>());
        for (int j = 0; j < n; j++) {
            e[i].push_back(0);
            r[i].push_back(0);
        }
    }
    
    int u, v, c;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> c;
        a[u].push_back(v);
        a[v].push_back(u);
        e[u][v] = c;
    }

    int par[M];
    int mx = 0;

    while (bfs(a, e, par, s, t)) {

        int f = INT32_MAX;
        for (v = t; v != s; v = par[v]) {
            u = par[v];
            f = min(f, e[u][v]);
        }

        for (v = t; v != s; v = par[v]) {
            u = par[v];
            r[u][v] += f;
            r[v][u] -= f;
            e[u][v] -= f;
            e[v][u] += f;
        }

        mx += f;

    }

    vector<tuple<int, int, int>> vs;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (r[i][j] > 0)
                vs.push_back(make_tuple(i, j, r[i][j]));

    cout << n << " " << mx << " " << vs.size() << endl;

    for (int i = 0; i < vs.size(); i++) {
        cout << get<0>(vs[i]) << " " << get<1>(vs[i]) << " " << get<2>(vs[i]) << endl;
    }

    return 0;

}
