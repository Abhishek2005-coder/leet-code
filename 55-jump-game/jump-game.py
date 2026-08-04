class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0
        
        for i, jump in enumerate(nums):
            # If the current index is beyond the maximum index we can reach, we're stuck
            if i > max_reachable:
                return False
            
            # Update the farthest index we can reach from here
            max_reachable = max(max_reachable, i + jump)
            
            # Early exit if we can already reach or surpass the final index
            if max_reachable >= len(nums) - 1:
                return True
                
        return True