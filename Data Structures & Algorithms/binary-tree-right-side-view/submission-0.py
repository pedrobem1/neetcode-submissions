# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            res = []

            q = collections.deque()
            q.append(root)

            while q:
                qLen = len(q)
                level = []
                for _ in range(qLen):
                    node = q.popleft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                if level:
                    res.append(level)
                
            return res
        vis_right = []
        levels = levelOrder(self,root)
        for level in levels:
            vis_right.append(level[-1])
        return vis_right
