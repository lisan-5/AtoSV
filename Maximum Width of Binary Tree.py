class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = [(root, 0)]

        while queue:
            level_length = len(queue)
            _, first_index = queue[0]

            for i in range(level_length):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
                    
            max_width = max(max_width, index - first_index + 1)

        return max_width
