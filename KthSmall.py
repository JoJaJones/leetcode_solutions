class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.kth_small(root, k, 0)[1]
    
    def kth_small(self, node, k, n):
        if node.left:
            is_done, n = self.kth_small(node.left, k, n)
            if is_done:
                return is_done, n
        
        n += 1
        if n == k:
            return True, node.val
        
        if node.right:
            is_done, n = self.kth_small(node.right, k, n)
            return is_done, n
        
        return False, n
