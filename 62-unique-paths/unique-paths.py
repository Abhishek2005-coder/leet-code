class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Initialize a row with 1s since there's only 1 way to reach any cell in the first row
        row = [1] * n
        
        for i in range(m - 1):
            new_row = [1] * n
            for j in range(1, n):
                # Unique paths to cell (i, j) = paths from above + paths from left
                new_row[j] = new_row[j - 1] + row[j]
            row = new_row
            
        return row[-1]