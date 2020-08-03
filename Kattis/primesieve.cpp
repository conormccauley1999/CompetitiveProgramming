#include <bits/stdc++.h>
#define M 100000001

typedef long long ll;
using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, q;
    cin >> n >> q;

    bitset<M> &ps = *(new bitset<M>());
    ps.set();
    ps[0] = ps[1] = 0;

    for (int i = 2; i <= n; i++)
        if (ps[i] && (ll) i * i <= n)
            for (int j = i * i; j <= n; j += i)
                ps[j] = false;

    int t = 0;
    for (int i = 2; i <= n; i++)
        if (ps[i]) t++;
    
    cout << t << endl;

    int x;
    for (int i = 0; i < q; i++) {
        cin >> x;
        cout << (ps[x] ? 1 : 0) << endl;
    }

    return 0;

}
