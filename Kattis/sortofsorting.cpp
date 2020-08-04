#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    while (true) {

        cin >> n;
        if (!n) break;

        vector<pair<string, int>> vs;
        vector<string> ss;

        string s;
        for (int i = 0; i < n; i++) {
            cin >> s;
            vs.push_back(make_pair(s.substr(0, 2), i));
            ss.push_back(s);
        }

        sort(vs.begin(), vs.end());
        
        for (int i = 0; i < n; i++) {
            cout << ss[vs[i].second] << endl;
        }

        cout << endl;

    }

    return 0;

}
