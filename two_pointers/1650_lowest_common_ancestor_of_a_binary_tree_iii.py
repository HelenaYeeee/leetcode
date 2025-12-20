"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def find_depth(p):
            # return the depth level of node p 
            depth_level = 0 
            current_node = p

            while current_node.parent: 
                current_node = current_node.parent
                depth_level += 1
            
            return depth_level 
        

        
        
        

        # 1. find depth of p and q 
        p_depth = find_depth(p)
        q_depth = find_depth(q)

        # 2. move the lower node up the tree until it is at the same level as the other one 
        while p_depth > q_depth: 
            p = p.parent
            p_depth -= 1
        
        while q_depth > p_depth: 
            q = q.parent
            q_depth -= 1
        
        # after the two while loop, p_depth = q_depth 

        # 3. move both node up by one level, repeat until they meet 
        while p.val != q.val: 
            p = p.parent 
            q = q.parent 
        
        return p # do not return p.val! The function declaration expects the output as type "Node"


