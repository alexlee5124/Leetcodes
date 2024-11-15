# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxHeight = 0
        root.val = 1
        nodeQueue = [root]
        while nodeQueue:
            curNode = nodeQueue.pop(-1)
            if curNode.left is not None:
                curNode.left.val = curNode.val + 1
                nodeQueue.insert(0, curNode.left)
            if curNode.right is not None:
                curNode.right.val = curNode.val + 1
                nodeQueue.insert(0, curNode.right)
            if curNode.val > maxHeight:
                maxHeight = curNode.val
        return maxHeight
