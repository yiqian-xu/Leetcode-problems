# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        if not root:return 0
        #if root.val equals to or smaller than L, the possible nodes that are within the range of [L,R] only exists in root's right branch
        #if root.val equals to or greater than R, the possible nodes that are within the range of [L,R] only exists in root's left branch
        if root.val is within [L,R], the possible nodes that are within the range of [L,R] exists in both root's left and right branch
        
        if root.val==L:
            return root.val+self.rangeSumBST(root.right,L,R)
        if root.val==R:
            return root.val+self.rangeSumBST(root.left,L,R)
        if root.val>R:
            return self.rangeSumBST(root.left,L,R)
        if root.val<L:
            return self.rangeSumBST(root.right,L,R)
        if L<root.val<R:
            return root.val+self.rangeSumBST(root.right,L,R)+self.rangeSumBST(root.left,L,R)
