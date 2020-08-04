#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    vector<int> vs(n);
    for (int i = 0; i < n; i++)
        cin >> vs[i];

    sort(vs.begin(), vs.end(), greater<int>());

    int t = 0;
    int r = n % 3;

    for (int i = 0; i < n - r; i += 3)
        t += vs[i] + vs[i + 1];
    
    for (int i = n - r; i < n; i++)
        t += vs[i];

    cout << t << endl;

    return 0;

}
