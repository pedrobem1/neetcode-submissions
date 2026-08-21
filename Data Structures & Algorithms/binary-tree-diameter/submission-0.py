# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx = 0
        def dfs(node):
            nonlocal maxx
            if node is None:
                return -1
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            d = left + right
            if d > maxx:
                maxx = d
            return max(left , right)
        dfs(root)
        return maxx