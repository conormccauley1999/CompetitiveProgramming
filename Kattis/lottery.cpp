#include <bits/stdc++.h>
#define M 1001

typedef long double ld;
using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int total_entries, total_draws, tickets_per_winner, our_entries;
    cin >> total_entries >> total_draws >> tickets_per_winner >> our_entries;

    int needed_wins = (int) ceil((ld) our_entries / (ld) tickets_per_winner);

    ld** dp = new ld*[M];
    for (int i = 0; i < M; i++)
        dp[i] = new ld[M];
    dp[0][0] = 1.0;

    for (int cur_draw = 0; cur_draw < total_draws; cur_draw++) {

        int total_remaining = total_entries - cur_draw;

        for (int cur_wins = 0; cur_wins < our_entries; cur_wins++) {

            int our_remaining = our_entries - cur_wins;
            ld prob_win = (ld) our_remaining / (ld) total_remaining;

            dp[cur_draw + 1][cur_wins] += dp[cur_draw][cur_wins] * (1 - prob_win);
            dp[cur_draw + 1][cur_wins + 1] += dp[cur_draw][cur_wins] * prob_win;

        }

        dp[cur_draw + 1][our_entries] += dp[cur_draw][our_entries];

    }

    ld total_prob = 0.0;
    for (int wins = needed_wins; wins <= our_entries; wins++) {
        total_prob += dp[total_draws][wins];
    }

    printf("%.20Lf\n", total_prob);

    return 0;

}
