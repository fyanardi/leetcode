class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(nodes: list[int | None]) -> TreeNode | None:
    """
    Helper function to build binary tree from a list of int values (not part of the solution)
    """
    if len(nodes) == 0:
        return None

    root_val = nodes.pop(0)
    assert root_val is not None

    root_node = TreeNode(root_val)
    tree_nodes: list[TreeNode] = [root_node]

    while len(nodes) > 0:
        tree_node = tree_nodes.pop(0)
        left_val = nodes.pop(0)
        if left_val is not None:
            tree_node.left = TreeNode(left_val)
            tree_nodes.append(tree_node.left)

        right_val = nodes.pop(0)
        if right_val is not None:
            tree_node.right = TreeNode(right_val)
            tree_nodes.append(tree_node.right)

    return root_node


def print_binary_tree(node: TreeNode | None, indent: int):
    """
    Helper function to print binary tree values from a root node (not part of the solution)
    """
    if node is not None:
        tabs = ''.join([' '] * 4 * indent) if indent > 0 else ''
        print(f"{tabs}node val={node.val} left={node.left} right={node.right}")
        print_binary_tree(node.left, indent + 1)
        print_binary_tree(node.right, indent + 1)



