class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_view = []
        queue = [root]
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                if i == level_length - 1:
                    right_view.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view
