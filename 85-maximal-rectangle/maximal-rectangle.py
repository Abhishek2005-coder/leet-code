class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Update histogram heights for the current row
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
                    
            # Calculate maximum rectangle area for the current histogram
            stack = []
            for i in range(cols + 1):
                h = 0 if i == cols else heights[i]
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
                
        return max_area