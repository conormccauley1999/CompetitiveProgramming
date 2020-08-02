#include <bits/stdc++.h>

using namespace std;
const int M = 200000;

int main() {

    int N, t;
    int A[M];

    cin >> N >> t;

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    if (t == 1) {
        cout << 7 << endl;
    } else if (t == 2) {
        if (A[0] > A[1])
            cout << "Bigger" << endl;
        else if (A[0] == A[1])
            cout << "Equal" << endl;
        else
            cout << "Smaller" << endl;
    } else if (t == 3) {
        vector<int> v;
        v.push_back(A[0]);
        v.push_back(A[1]);
        v.push_back(A[2]);
        sort(v.begin(), v.end());
        cout << v[1] << endl;
    } else if (t == 4) {
        long long s = 0;
        for (int i = 0; i < N; i++) {
            s += A[i];
        }
        cout << s << endl;
    } else if (t == 5) {
        long long s = 0;
        for (int i = 0; i < N; i++) {
            if (A[i] % 2 == 0)
                s += A[i];
        }
        cout << s << endl;
    } else if (t == 6) {
        string s = "abcdefghijklmnopqrstuvwxyz";
        for (int i = 0; i < N; i++) {
            cout << s[A[i] % 26];
        }
        cout << endl;
    } else {
        bool v[M] = {0};
        int i = 0;
        while (true) {
            i = A[i];
            if (i < 0 || i >= N) {
                cout << "Out" << endl;
                return 0;
            } else if (v[i]) {
                cout << "Cyclic" << endl;
                return 0;
            } else if (i == N - 1) {
                cout << "Done" << endl;
                return 0;
            }
            v[i] = true;
        }
    }

    return 0;

}
