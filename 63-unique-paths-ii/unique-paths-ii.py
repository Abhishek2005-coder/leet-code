class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1  # Starting point
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Obstacle blocks any paths through this cell
                elif j > 0:
                    dp[j] += dp[j - 1]  # Paths from above (dp[j]) + paths from left (dp[j-1])
                    
        return dp[-1]