class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # Early exit if target is longer than source
        if m < n:
            return 0
            
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: An empty t can be formed in 1 way from any prefix of s
        for i in range(m + 1):
            dp[i][0] = 1
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                    
        return dp[m][n]