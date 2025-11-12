from typing import List
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        one_count = 0
        cur_gcd = 0
        for n in nums:
            if n == 1:
                one_count += 1
            cur_gcd = gcd(cur_gcd, n)
        if one_count > 0:
            return len(nums) - one_count
        if cur_gcd != 1:
            return -1

        min_sub_len = float("inf")
        for i in range(len(nums)):
            cur = 0
            for r in range(i, len(nums)):
                if r - i + 1 >= min_sub_len:
                    break
                cur = gcd(cur, nums[r])
                if cur == 1:
                    min_sub_len = r - i + 1
                    break
        return (min_sub_len - 1) + len(nums) - 1
