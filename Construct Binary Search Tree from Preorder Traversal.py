class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for value in preorder[1:]:
            node, child = stack[-1], TreeNode(value)
            
            while stack and stack[-1].val < value:
                node = stack.pop()
                
            if value < node.val:
                node.left = child
            else:
                node.right = child
                
            stack.append(child)
        
        return root
