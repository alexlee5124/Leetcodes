/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        root.val = 1;
        int maxHeight = 0;
        ArrayList<TreeNode> nodeQueue = new ArrayList<TreeNode>() {{add(root);}};
        while (!nodeQueue.isEmpty()) {
            TreeNode curNode = nodeQueue.remove(0);
            if (curNode.left != null) {
                curNode.left.val = curNode.val + 1;
                nodeQueue.add(curNode.left);
            }
            if (curNode.right != null) {
                curNode.right.val = curNode.val + 1;
                nodeQueue.add(curNode.right);
            }
            if (curNode.val > maxHeight) {
                maxHeight = curNode.val;
            }
        }
        return maxHeight;
    }
}
