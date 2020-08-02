#include <iostream>
#include <vector>

typedef long long ll;
using namespace std;

vector<ll> v;
vector<ll> s;

int f(int i) {
    if (i == v[i])
        return i;
    return v[i] = f(v[i]);
}

void u(int a, int b) {

    a = f(a);
    b = f(b);

    if (a == b)
        return;
    
    if (s[a] < s[b]) swap(a, b);
    v[b] = a;
    s[a] += s[b];

}

bool c(int a, int b) {
    return f(a) == f(b);
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    ll n, q;
    cin >> n >> q;

    v.resize(n, 0);
    s.resize(n, 0);

    for (int i = 0; i < n; i++) {
        v[i] = i;
        s[i] = 1;
    }

    char o;
    ll a, b;
    for (int i = 0; i < q; i++) {
        cin >> o >> a >> b;
        if (o == '=') u(a, b);
        else {
            if (c(a, b))
                cout << "yes\n";
            else
                cout << "no\n";
        }
    }
    
    return 0;

}
