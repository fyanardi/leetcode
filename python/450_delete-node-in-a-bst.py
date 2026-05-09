from helpers.binarytree import (
    TreeNode,
    parse_binary_tree,
    serialize_binary_tree,
)


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def delete_node(root: TreeNode | None, key: int) -> TreeNode | None:
            if root is None:
                return None

            if root.val == key:
                if root.left is not None and root.right is not None:
                    # Need to ensure the BST structure is still correct that the replaced root node is less than it's
                    # left node and greater than it's right node
                    # Replace the root with it's right node (which is already greater than the left node)
                    node = root.right
                    # However if the right node has children / grandchildren, find the left most leaf node, since that
                    # node will have the smallest value among all other right nodes, and hence will fulfill the BST
                    # structure
                    while node.left is not None:
                        node = node.left
                    node.right = delete_node(root.right, node.val)
                    node.left = root.left
                    return node
                elif root.left is not None:
                    node = root.left
                    return node
                elif root.right is not None:
                    node = root.right
                    return node
                else:
                    return None
            elif key > root.val:
                root.right = delete_node(root.right, key)
                return root
            else:
                root.left = delete_node(root.left, key)
                return root

        return delete_node(root, key)


if __name__ == "__main__":
    solution = Solution()

    # [5, 2, 6, None, 4, None, 7] should also be accepted as a valid answer
    assert serialize_binary_tree(
        root=solution.deleteNode(parse_binary_tree([5, 3, 6, 2, 4, None, 7]), 3)
    ) == [5, 4, 6, 2, None, None, 7]

    assert serialize_binary_tree(
        root=solution.deleteNode(parse_binary_tree([5, 3, 6, 2, 4, None, 7]), 0)
    ) == [5, 3, 6, 2, 4, None, 7]

    assert serialize_binary_tree(
        root=solution.deleteNode(parse_binary_tree([]), 0)
    ) == []

    assert serialize_binary_tree(
        root=solution.deleteNode(parse_binary_tree([50, 30, 70, None, 40, 60, 80]), 50)
    ) == [60, 30, 70, None, 40, None, 80]
