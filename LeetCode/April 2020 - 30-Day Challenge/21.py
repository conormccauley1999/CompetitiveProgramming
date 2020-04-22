# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        INF = 10 ** 12
        N, M = binaryMatrix.dimensions()
        r = INF
        for x in range(N):
            l, h = 0, M - 1
            while h >= l:
                y = l + (h - l) // 2
                if binaryMatrix.get(x, y) == 1:
                    r = min(r, y)
                    h = y - 1
                else:
                    l = y + 1
        return -1 if r == INF else r
