# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            q = collections.deque()
            q.append(root)
            res = []
            while q:
                qLen = len(q)
                level = []
                for _ in range(qLen):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level.append(node.val)

                if level:
                    res.append(level)
            return res

        if not root:
            return []

        vector = bfs(root)
        answer = []
        for level in vector:
            answer.append(level[-1])
        
        return answer
        

