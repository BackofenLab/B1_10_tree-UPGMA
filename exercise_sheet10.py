


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