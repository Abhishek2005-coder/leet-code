class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        # dp[i][j] stores the edit distance between word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: converting string to empty string requires deletions
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # Characters match, no cost
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # Delete character from word1
                        dp[i][j - 1],     # Insert character into word1
                        dp[i - 1][j - 1]  # Replace character in word1
                    )
                    
        return dp[m][n]