from sorting import is_sorted
from binarytree import BinarySearchTree

items = [5, 8, 2, 0, 11, 4, 3, 9]
tree = BinarySearchTree(items)

print(tree.items_in_order())
