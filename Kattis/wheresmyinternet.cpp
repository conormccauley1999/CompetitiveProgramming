#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> adj;
vector<bool> vis;

void dfs(int x) {
    if (vis[x]) return;
    vis[x] = true;
    for (int i = 0; i < adj[x].size(); i++) dfs(adj[x][i]);
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        adj.push_back(vector<int>());
        vis.push_back(false);
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(0);

    vector<int> nvis;
    for (int i = 0; i < n; i++) {
        if (!vis[i]) nvis.push_back(i);
    }

    if (nvis.size()) {
        for (int x : nvis) cout << x + 1 << endl;
    } else {
        cout << "Connected" << endl;
    }

    return 0;

}
