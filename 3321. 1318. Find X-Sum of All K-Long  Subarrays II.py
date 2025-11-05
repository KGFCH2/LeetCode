from collections import defaultdict
from sortedcontainers import SortedList
from typing import List


class Solution:

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Find X-Sum of all K-long subarrays.
        X-Sum is the sum of x largest elements with highest frequencies in the subarray.
        """
        top = SortedList()  # (freq, num) - top x elements by frequency
        remain = SortedList()  # (freq, num) - remaining elements
        freq = defaultdict(int)  # num -> frequency
        cur_sum = 0

        def balance():
            """Balance elements between top and remain lists."""
            nonlocal cur_sum

            # Fill top list if it has less than x elements
            if len(top) < x and remain:
                f, n = remain.pop()
                top.add((f, n))
                cur_sum += f * n

            # Rebalance if smallest in top is less than largest in remain
            if top and remain and top[0] < remain[-1]:
                f1, n1 = top.pop(0)
                f2, n2 = remain.pop()
                top.add((f2, n2))
                remain.add((f1, n1))
                cur_sum += (f2 * n2) - (f1 * n1)

        def update(num, delta):
            """Update frequency of a number and rebalance."""
            nonlocal cur_sum

            if num in freq:
                old_freq = freq[num]
                if (old_freq, num) in top:
                    top.remove((old_freq, num))
                    cur_sum -= old_freq * num
                else:
                    remain.remove((old_freq, num))

            freq[num] += delta

            if freq[num] == 0:
                del freq[num]
            else:
                remain.add((freq[num], num))

            balance()

        res = []

        # Process first window
        for i in range(k):
            update(nums[i], 1)
        res.append(cur_sum)

        # Slide the window
        for i in range(k, len(nums)):
            update(nums[i - k], -1)
            update(nums[i], 1)
            res.append(cur_sum)

        return res