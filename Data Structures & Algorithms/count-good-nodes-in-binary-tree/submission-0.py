# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val) -> int:
            if node is None:
                return 0
                        

            if max_val <= node.val:
                max_val = node.val
                return (1 + dfs(node.left,max_val) + dfs(node.right,max_val))
            else:
                return (dfs(node.left,max_val) + dfs(node.right,max_val))

        
        return dfs(root,root.val)
