class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        return self.BFS(q) == self.BFS(p)
    
    def BFS(self, node):
        queue = [node]
        res = []
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
                res.append(cur.val)
            else:
                res.append(cur)
        
        return res
