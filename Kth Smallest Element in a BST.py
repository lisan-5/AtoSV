class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        return inorder(root)[k - 1]
