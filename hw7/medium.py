from easy import * # import my work from the easy.py homework assignment so I can use the tree I already created

# define function to serach for a value in the tree
def find(node, key):

    # if when we are searching for the node, the value isn't found...
    if node is None:

        # print false
        return False
    
    # if the value we are searching for finds a match in the tree
    if node.key == key:

        # print true
        return True

    # recur down the tree
    # if the key is less than the node
    if key < node.key: 

        # move to the left and call the function again to keep moving down the tree
        return find(node.left, key)

    # if the key is greater than the node
    else:

        # move to the right and call the function again to keep moving down the tree
        return find(node.right, key)

# Use the find function to search my tree for numbers
print(find(tree_Emmy, 80))
print(find(tree_Emmy, 120))
print(find(tree_Emmy, 100))
print(find(tree_Emmy, 10000))
