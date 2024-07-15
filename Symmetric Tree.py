class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and 
                    is_mirror(t1.right, t2.left) and 
                    is_mirror(t1.left, t2.right))
        
        return is_mirror(root, root)
