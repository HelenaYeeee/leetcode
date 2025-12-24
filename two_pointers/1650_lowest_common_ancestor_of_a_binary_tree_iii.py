# sol 1. finding depth of nodes (best)
# ref: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/solutions/1233986/python-find-depth-difference-explanation-w0la 

# time complexity: O(n) where n = depth of tree
# space complexity: O(1) becasue we didn't initialize any data structure 


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


# sol 2. use a set to store all nodes from p to root,
# then compare with all nodes from q to root
# the LCA will be the first common node between the two 

# time complexity: O(n) where n = depth of tree 
# space complexity: O(n) because of the set
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
        path = set()

        while p: 
            path.add(p)
            p = p.parent
        
        while q not in path: 
            q = q.parent
        return q 


