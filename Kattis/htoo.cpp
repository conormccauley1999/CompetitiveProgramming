#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string a, b;
    int k;

    cin >> a >> k;
    cin >> b;

    map<char, int> ac;
    map<char, int> bc;

    for (int i = 0; i < 26; i++) {
        ac.insert(make_pair(char(i + 65), 0));
        bc.insert(make_pair(char(i + 65), 0));
    }

    char cc = ' ';
    int cn = 0;

    for (char &c : a) {
        if (isdigit(c)) {
            cn *= 10;
            cn += int(c) - '0';
        } else {
            if (cc != ' ')
                ac[cc] += (cn != 0) ? cn : 1;
            cc = c;
            cn = 0;
        }
    }
    ac[cc] += (cn != 0) ? cn : 1;
    
    cc = ' ';
    cn = 0;

    for (char &c : b) {
        if (isdigit(c)) {
            cn *= 10;
            cn += int(c) - '0';
        } else {
            if (cc != ' ')
                bc[cc] += (cn != 0) ? cn : 1;
            cc = c;
            cn = 0;
        }
    }
    bc[cc] += (cn != 0) ? cn : 1;
    
    int m = INT32_MAX;
    
    for (int i = 0; i < 26; i++) {
        char c = char(i + 65);
        ac[c] *= k;
        if (bc[c] == 0)
            continue;
        if (ac[c] == 0) {
            m = 0;
            break;
        }
        m = min(m, ac[c] / bc[c]);
    }

    cout << m << endl;
    
    return 0;

}
