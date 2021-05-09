class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p = p.val
        q = q.val
        cur = root
        if p > q:
            p, q = q, p
        
        while not (p <= cur.val <= q):
            if p < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        
        return cur
