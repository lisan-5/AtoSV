class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_paths(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(node.left, path)
                    construct_paths(node.right, path)
                    
        paths = []
        construct_paths(root, "")
        return paths
