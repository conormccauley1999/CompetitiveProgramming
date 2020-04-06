class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, P, B, V = len(prices), 0, False, 0
        for i in range(0, L - 1):
            if not B and prices[i] < prices[i + 1]:
                B, V = True, prices[i]
            elif B and prices[i] > prices[i + 1]:
                P += prices[i] - V
                B, V = False, 0
        if B:
            P += prices[L - 1] - V
        return P
