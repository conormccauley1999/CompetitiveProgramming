#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while (t--) {

        int n;
        cin >> n;

        bool xs[n];
        int rs[n];
        int z = 0;

        list<int> e0;
        list<int> e1;

        for (int i = 0; i < n; i++) {

            char b;
            cin >> b;

            bool c = b == '1';

            if (c) {
                if (e0.size()) {
                    int j = e0.front();
                    e0.pop_front();
                    e1.push_back(j);
                    xs[j] = !xs[j];
                    rs[i] = j + 1;
                } else {
                    xs[i] = c;
                    e1.push_back(z);
                    z++;
                    rs[i] = z;
                }
            } else {
                if (e1.size()) {
                    int j = e1.front();
                    e1.pop_front();
                    e0.push_front(j);
                    xs[j] = !xs[j];
                    rs[i] = j + 1;
                } else {
                    xs[i] = c;
                    e0.push_back(z);
                    z++;
                    rs[i] = z;
                }
            }

        }

        cout << z << endl;
        for (int i = 0; i < n; i++)
            cout << rs[i] << " ";
        cout << endl;

    }

    return 0;

}
