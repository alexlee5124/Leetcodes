/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        root->val = 1;
        int maxHeight = 0;

        std::vector<TreeNode*> nodeQueue = {root};
        while (!nodeQueue.empty()) {
            TreeNode* curNode = nodeQueue[0];
            nodeQueue.erase(nodeQueue.begin());
            if (curNode->left != NULL) {
                curNode->left->val = curNode->val + 1;
                nodeQueue.push_back(curNode->left);
            }
            if (curNode->right != NULL) {
                curNode->right->val = curNode->val + 1;
                nodeQueue.push_back(curNode->right);
            }

            if (curNode->val > maxHeight) {
                maxHeight = curNode->val;
            }
        }
        return maxHeight;
    }
};
