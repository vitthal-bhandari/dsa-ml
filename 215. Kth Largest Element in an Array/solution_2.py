"""
This approach is called the Quickselect algorithm, which is a selection algorithm to find the k-th largest element in an unordered list.

It is related to the QuickSort sorting algorithm.

Time Complexity: O(N) on average, where N is the number of elements in the input array. In the worst case, it can degrade to O(N^2), but this is rare with random pivot selection.

Each call we make to quickSelect will cost O(n) since we need to iterate over nums to create left, mid, and right. The number of times we call quickSelect is dependent on how the pivots are chosen. The worst pivots to choose are the extreme (greatest/smallest) ones because they reduce our search space by the least amount. Because we are randomly generating pivots, we may end up calling quickSelect O(n) times, leading to a time complexity of O(n^2).

However, the algorithm mathematically almost surely has a linear runtime. For any decent size of nums, the probability of the pivots being chosen in a way that we need to call quickSelect O(n) times is so low that we can ignore it.

On average, the size of nums will decrease by a factor of ~2 on each call. You may think: that means we call quickSelect O(logn) times, wouldn't that give us a time complexity of O(n⋅logn)? Well, each successive call to quickSelect would also be on a nums that is a factor of ~2 smaller. This recurrence can be analyzed using the master theorem with a = 1, b = 2, k = 1:

T(n)=T(n/2)+O(n)=O(n)

Space Complexity: O(N) in the worst case due to the additional lists created during partitioning.

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        random_number = random.randint(0, len(nums)-1)
        pivot = nums[random_number]

        left, mid, right = [], [], []

        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)
        
        if len(left) >= k:
            return self.findKthLargest(left, k)
        elif len(left) + len(mid) < k:
            return self.findKthLargest(right, k - len(left) - len(mid))
        else:
            return pivot