#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    long n;
    cin >> n;

    long mx = 0;
    long r = 0;
    long bmx = max(n, 1000001L);
    
    for (long b = 2; b <= bmx; b++) {
        long m = n;
        int c = 0;
        while (!(m % b)) {
            m /= b;
            c++;
        }
        if (c > mx) {
            mx = c;
            r = b;
        }
    }

    cout << r << endl;

    return 0;

}
