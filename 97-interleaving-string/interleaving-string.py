class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        
        # Length check
        if m + n != len(s3):
            return False
            
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Fill first column (only using s1)
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            
        # Fill first row (only using s2)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the rest of the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = from_s1 or from_s2
                
        return dp[m][n]