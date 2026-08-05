class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] represents the number of unique BSTs that can be formed using i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Empty tree is 1 combination
        dp[1] = 1  # Single-node tree is 1 combination
        
        # Fill dp array for each number of nodes from 2 to n
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_subtrees = dp[root - 1]
                right_subtrees = dp[nodes - root]
                dp[nodes] += left_subtrees * right_subtrees
                
        return dp[n]