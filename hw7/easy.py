# print_tree.py contains a print pretty version of a bst - got from data5510_fall2026 code
from print_tree import * 

# define funtion to insert a value
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
    # if the key is less than the node...
	if key < node.key:

        # from the left node, recur and call the function again on the left node
		node.left = insert(node.left, key)

    # if the key is greater than the node
	else:

        # from the right node, recur and call the function again on the right node
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node


# A Binary Tree Node - code from data5510_fall2026 to create a class called Node
class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# create a tree using the insert function
tree_Emmy = None
tree_Emmy = insert(tree_Emmy, 26)
tree_Emmy = insert(tree_Emmy, 16)
tree_Emmy = insert(tree_Emmy, 12)
tree_Emmy = insert(tree_Emmy, 2)
tree_Emmy = insert(tree_Emmy, 100)
tree_Emmy = insert(tree_Emmy, 120)
tree_Emmy = insert(tree_Emmy, 66)
tree_Emmy = insert(tree_Emmy, 62)
tree_Emmy = insert(tree_Emmy, 20)
tree_Emmy = insert(tree_Emmy, 22)
tree_Emmy = insert(tree_Emmy, 102)
tree_Emmy = insert(tree_Emmy, 122)

# display the tree
display(tree_Emmy)