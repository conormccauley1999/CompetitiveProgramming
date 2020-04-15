class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            new_stones = []
            if stones[0] != stones[1]:
                new_stones.append(stones[0] - stones[1])
            if len(stones) > 2:
                new_stones.extend(stones[2:])
            stones = new_stones
        return 0 if len(stones) == 0 else stones[0]
