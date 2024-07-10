class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        count = collections.Counter(inorder(root))
        max_freq = max(count.values())
        return [k for k, v in count.items() if v == max_freq]
