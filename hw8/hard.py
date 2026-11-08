# Write a Python function that takes a NetworkX graph as input and returns the number of 
# nodes in the graph that have a degree greater than 5

# import libraries
import networkx as nx
import os

#----------------------- Open File and Create Directed Graph -----------------------#
# Loading edges of the Graph from a file (code from data5510_fall2026)
curr_dir = os.path.dirname(__file__) # get the current directory of this file

edges_fil = curr_dir + "/" + "edges.txt" # dirname and __file__ (this file) returns the current folder
graph_visual_fil = curr_dir + "/" + "graph_visual.png"

file = open(edges_fil) 

g = nx.DiGraph() # created directed graph

# --------------------- Create Graph From Information in File ------------------------#
# Create Graph (copied code to create graph from data5510_fall2026 and added comments)

# get all edges from the txt file
edges = []

# for each line in the file...
for line in file.readlines():

    # split the data by the commas
    node1, node2, weight = line.split(",")

    # change it to an integer
    weight = int(weight)

    # append the information to the edges list
    edges.append((node1, node2, weight)) # add edge to a list of tuples

# use the tuples created to build the graph
g.add_weighted_edges_from(edges)

#-------------- Use the Function count_nodes to Find How Many Nodes Have A Degree Greater Than 5 ----------------#
# define function
def count_nodes(graph):

    # establish starting variable
    count = 0

    # for each node and degree in the graph...
    for node, degree in graph.degree(): # AI was used to help understand how to find the degree and write this line of code

        # if the degree is greater than 5
        if degree > 5:

            # keep track by adding one to the count
            count += 1

    return count

# call the function
num_nodes = count_nodes(g)

# print the output
print(f"There are {num_nodes} nodes in this graph that have a degree greater than 5.")




