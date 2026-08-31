# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []
        count = 0
        
        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    if(count % 2 ==0):
                        level.append(node.val)
                    else:
                        level.insert(0,node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

            count += 1

        return res

