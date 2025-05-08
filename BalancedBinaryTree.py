class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(node):
            if not node:
                return 0
            
            left = balanced(node.left)
            if left == float('inf'):
                return float('inf')
            right = balanced(node.right)
            if right == float('inf'):
                return float('inf')

            if abs(left - right) > 1:
                return float('inf')
            
            return max(left, right) + 1

        return balanced(root) != float('inf')
