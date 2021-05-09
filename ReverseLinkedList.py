class Solution(object):
    def reverseList(self, node, prev=None):
        return self.o_1_space(node)
        # return self.o_n_space(node)
        # return self.recursive(node, None)
    
    def recursive(self, node, prev):
        if node is None:
            return None
        elif node.next is None:
            node.next = prev
            return node
        else:
            next_node = node.next
            node.next = prev
            return self.reverseList(next_node, node)
    
    def o_1_space(self, node):
        if not node:
            return None
        next_node = None
        cur = node
        prev = cur.next
        while prev:
            cur.next = next_node
            next_node = cur
            cur = prev
            prev = prev.next
        cur.next = next_node
        return cur
    
    def o_n_space(self, node):
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i-1]
        if len(nodes) > 0:
            nodes[0].next = None
            return nodes[-1]
        else:
            return None
