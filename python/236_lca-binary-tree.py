# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # level of each node in the binary tree
        levels = { root: 0 }
        # parent node
        parents = {}
        # Do a BFS search to find out the level of p and q
        frontier = [root]
        while frontier:
            node = frontier[0]
            frontier = frontier[1:]

            # Once both p and q are found, break the BFS
            if p in levels and q in levels:
                break
            if node.left:
                levels[node.left] = levels[node] + 1
                parents[node.left] = node
                frontier.append(node.left)
            if node.right:
                levels[node.right] = levels[node] + 1
                parents[node.right] = node
                frontier.append(node.right)

        # Check which node is higher up in the tree, and assign it to ancestor0
        ancestor0 = None
        ancestor1 = None
        lower_node = None
        target_level = -1

        if levels[p] < levels[q]:
            ancestor0 = p
            lower_node = q
            target_level = levels[p]
        elif levels[p] > levels[q]:
            ancestor0 = q
            lower_node = p
            target_level = levels[q]
        else:
            # Both p and q are at the same level
            ancestor0 = p
            ancestor1 = q

        # If the level of both p and q are different, find the ancestor of the lower node (node with
        # higher node level) that is of the same level as the upper node
        if lower_node:
            ancestor1 = lower_node
            while levels[ancestor1] > target_level:
                ancestor1 = parents[ancestor1]

        # Finally find the common ancestor between the two. It is possible that before entering the
        # loop both ancestor0 and ancestor1 are already the same. This indicates one node is a
        # descendant of the other node
        while ancestor0 != ancestor1:
            ancestor0 = parents[ancestor0]
            ancestor1 = parents[ancestor1]

        if ancestor0 == ancestor1:
            return ancestor0
        else:
            return None

