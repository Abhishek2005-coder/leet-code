# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
        
        memo = {}
        
        def build_trees(start, end):
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            
            # Pick every number as the root node
            for i in range(start, end + 1):
                # Recursively generate all left and right subtrees
                left_subtrees = build_trees(start, i - 1)
                right_subtrees = build_trees(i + 1, end)
                
                # Combine left and right subtrees with root i
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            memo[(start, end)] = all_trees
            return all_trees
        
        return build_trees(1, n)