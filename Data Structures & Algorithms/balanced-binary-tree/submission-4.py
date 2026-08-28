# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            return 1 + max(left,right)

        def is_height_bal(node):
            if node is None:
                return True
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            left = is_height_bal(node.left)
            right = is_height_bal(node.right)
            if abs(left_height - right_height) <= 1 and left and right:
                return True
            else:
                return False
        
        return is_height_bal(root)


            

        
