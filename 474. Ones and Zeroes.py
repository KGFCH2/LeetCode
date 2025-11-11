from collections import defaultdict

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)

        for s in strs:
            mCnt, nCnt = s.count("0"), s.count("1")
            for i in range(m, mCnt - 1, -1):
                for j in range(n, nCnt - 1, -1):
                    dp[(i, j)] = max(
                        1 + dp[(i - mCnt, j - nCnt)],
                        dp[(i, j)])
        return dp[(m, n)]
        
