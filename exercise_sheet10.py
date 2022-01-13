


def exercise_1a():
    """
    Use the distance matrix from the Readme to select which leaves should be
    joined for an internal node first.
    """
    one = "c and d"
    two = "a and b"
    three = "d and e"
    return None


def exercise_1b():
    """
    Calculate the corresponding distance from the leaves to the internal Node
    selected in a.
    """
    distance = None
    return distance


def exercise_1c() -> int:
    """
    Which of the distance matrices represents the new one including the
    internal node from a.
    Return either 1, 2 or 3
    """
    return None


def exercise_1d():
    """
    Which nodes are joined next given the correct distance matrix from c?
    """
    one = "c and d"
    two = "{a,b} and e"
    three = "{c,d} and e"
    four = "e and a"
    return None


def exercise_1e():
    """
    Fill in the following distance matrix. (both, upper and lower triangle)
    """
    #    {a,b}, {c,d}, e
    matrix = [
            [0,    0,  0],  # {a,b}
            [0,    0,  0],  # {c,d}
            [0,    0,  0],  # e
    ]
    return matrix


def exercise_1f():
    """
    What does the part of the tree look like in newick format after selecting
    and joining your answer from e)
    """
    one = "((c : 3, d : 3) : 3.5, e : 3.5)"
    two = "((c : 3, d : 3) : 0.5, e : 3.5)"
    three = "((a : 1.5, b : 1.5) : 2.75, e : 4.25)"
    return None


def exercise_1g():
    """
    Given the initial distance matrix and the WPGMA function, which tree
    representation is correct?
    """
    one = "((a : 1.5, b : 1.5) : 4, ((c : 3, d : 3) : 0.5, e : 3.5) : 2);"
    two = "((a : 1.5, b : 1.5) : 4.25, ((c : 3, d : 3) : 0.5, e : 3.5) : 2.25);"
    three = "(((c : 3, d : 3) : 3.5, e : 3.5): 4, (a : 1.5, b : 1.5) : 2);"
    return None


def exercise_2a():
    """
    Imagine using  UPGMA instead of WPGMA for construction of a tree.
    Which of the following statements is True?
    """
    # There will only be a difference in edge lengths. Overall topology will
    # stay the same.
    one = None

    # The tree in Exercise 1 will not change
    two = None

    # UPGMA is equal to WPGMA if the number of leaves in the two clusters
    # (|c| and |d|) is the same.
    three = None

    # UPGMA can end up with wrong topologies when using non-ultrametric
    # distances.
    four = None

    return one, two, three, four

def exercise_3a():
    """
    Which of the following distance matrices are ultrametric?

    If a matrix is ultrametric label it as True, otherwise use False.
    """


    #a | 0 | 3 | 12 | 12 |  9 |
    #b |   | 0 | 13 | 13 | 10 |
    #c |   |   |  0 |  6 |  7 |
    #d |   |   |    |  0 |  7 |
    #e |   |   |    |    |  0 |
    a = None

    #a | 0 | 2 | 4 | 6 | 8 |
    #b |   | 0 | 4 | 6 | 8 |
    #c |   |   | 0 | 6 | 8 |
    #d |   |   |   | 0 | 8 |
    #e |   |   |   |   | 0 |
    b = None

    #a | 0 | 10 | 17 | 16 | 16 |
    #b |   |  0 | 15 | 14 | 14 |
    #c |   |    |  0 |  9 | 15 |
    #d |   |    |    |  0 | 14 |
    #e |   |    |    |    |  0 |
    c = None

    #a | 0 | 2 | 2 | 2 | 2 |
    #b |   | 0 | 4 | 4 | 4 |
    #c |   |   | 0 | 6 | 6 |
    #d |   |   |   | 0 | 8 |
    #e |   |   |   |   | 0 |
    d = None

    return a, b, c, d


########################################################
############## Programming tasks #######################
########################################################

from helpers import compute_distance
from helpers import Node
from helpers import Tree


"""
In all of the tasks we will use the same structure of the given data which can be seen as three parts
1. matrix of distances between nodes
2. names of the nodes
3. wpgma/upgma mode

These three components are merged into a "distance info" tuple for our convenience
"""
matrix_dist_1 = [[0, 3, 12, 12, 9], [3, 0, 13, 13, 10], [12, 13, 0, 6, 7], [12, 13, 6, 0, 7], [9, 10, 7, 7, 0]]
nodes_1 = ["a", "b", "c", "d", "e"]
weight_1 = "wpgma"
distance_info1 = matrix_dist_1, nodes_1, weight_1


"""
You are provided with one helper function and two helper classes to perform the tree assembly
compute_distance - computes the distance between two objects, it works for both Nodes and Trees for both wpgma and upgma
modes.
Node - a helper class to convert initial data into a node
Tree - a tree representation class wich can be printed with Newick's representation

Lets start creating nodes and trees
"""

a = Node("a", distance_info1)
b = Node("b", distance_info1)
first_tree = a + b
print("Nodes a and b", a, b)
print("Distance between nodes a and b is", compute_distance(a, b))
print(type(a))
print("Result of merging two nodes a and is a tree", first_tree)
print(type(a+b))

c = Node("c", distance_info1)
d = Node("d", distance_info1)
second_tree = c + d
print("Distance between nodes c and d is", compute_distance(c, d))
print("Result of merging two nodes c and is d tree", second_tree)

merged_trees = first_tree + second_tree
print("Distance between trees  (a,b) and (c,d) is", compute_distance(first_tree, second_tree))
print("Result of merging together two trees", merged_trees)


def convert_to_nodes(list_names, distance_info):
    """ Exercise 4 a
    implement the funcion 'convert_to_nodes' which takes a list of node names
    and converts it to list of nodes using the provided distance info
    """
    list_nodes = []
    return list_nodes


def merge_best_pair(list_elements):
    """ Exercise 4 b
    Implement the function 'merge_best_pair' which takes a list of elements
    which can be both nodes and trees, findes the best pair to merge based on
    the distance, merges two closest objects and returns a list with the mered
    object as well as the remaining ones use compute_distance for that purpose
    """
    list_after_merge = []
    return list_after_merge


def build_the_tree(list_names, distance_info):
    """ Exercise 4 c
    Implement the function 'build_the_tree' which takes the list of nodes names
    as well as the distance_info and outputs the final tree use your
    implementations of convert_to_nodes and merge_best_pair
    """
    tree = None
    return tree
