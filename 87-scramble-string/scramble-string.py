class Solution(object):
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Base Cases
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):  # Anagram pruning
            return False
        
        state = (s1, s2)
        if state in self.memo:
            return self.memo[state]
            
        n = len(s1)
        
        # Try splitting s1 and s2 at every possible index i
        for i in range(1, n):
            # Case 1: Without swapping
            # s1[0:i] matches s2[0:i] AND s1[i:] matches s2[i:]
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.memo[state] = True
                return True
                
            # Case 2: With swapping
            # s1[0:i] matches s2[n-i:] AND s1[i:] matches s2[0:n-i]
            if self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(s1[i:], s2[:n - i]):
                self.memo[state] = True
                return True
                
        self.memo[state] = False
        return False