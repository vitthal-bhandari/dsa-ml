"""
In this approach, we use the Counting Sort algorithm to find the k-th largest element in the array.

Given n as the length of nums and m as maxValue - minValue,

Time complexity: O(n+m)

We first find maxValue and minValue, which costs O(n).

Next, we initialize count, which costs O(m).

Next, we populate count, which costs O(n).

Finally, we iterate over the indices of count, which costs up to O(m).

Space complexity: O(m)

We create an array count with size O(m).
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)
        len_count = max_val - min_val + 1
        count = [0] * len_count

        for n in nums:
            count[n-min_val] += 1
        
        for i in range(len_count-1, -1, -1):
            k -= count[i]
            if k <= 0:
                return i + min_val
        
        return -1