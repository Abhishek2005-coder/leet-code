class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Start with the last row as our DP array
        dp = list(triangle[-1])
        
        # Iterate from the second-to-last row up to the top row
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                # Minimum path sum at cell (i, j) is its value plus 
                # the smaller of the two adjacent values below it
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
                
        return dp[0]