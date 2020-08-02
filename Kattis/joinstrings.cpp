#include <bits/stdc++.h>

using namespace std;

void rec(vector<vector<int>> &v, vector<string> &s, int a) {
    cout << s[a];
    for (int i : v[a])
        rec(v, s, i);
}

int main() {

    int n, a, b;

    cin >> n;
    vector<string> s(n);

    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }

    vector<vector<int>> v;
    v.assign(n, vector<int>());

    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        a--;
        b--;
        v[a].push_back(b);
    }

    rec(v, s, a);
    cout << endl;

    return 0;

}
