"""
This aproach uses a min-heap to keep track of the k largest elements seen so far.

Time Complexity: O(N log k), where N is the number of elements in the input array.

For each of the N elements, we perform a heap operation (either push or replace) which takes O(log k) time.

Space Complexity: O(k), since we are storing k elements in the heap.
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for n in nums:
            if len(q) == k:
                if n > q[0]:
                    heapq.heapreplace(q, n)
            else:
                heapq.heappush(q, n)
        return q[0]