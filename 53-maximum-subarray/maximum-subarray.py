class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            # Either extend the previous subarray or start a new subarray from the current number
            current_sum = max(num, current_sum + num)
            # Update the global maximum sum found so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum