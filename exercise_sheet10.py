


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
    Given the initial distance matrix and the WPGMA function, which tree
    representation is correct?
    """
    one = "((a : 1.5, b : 1.5) : 4, ((c : 3, d : 3) : 0.5, e : 3.5) : 2);"
    two = "((a : 1.5, b : 1.5) : 4.25, ((c : 3, d : 3) : 0.5, e : 3.5) : 2.25);"
    three = "(((c : 3, d : 3) : 3.5, e : 3.5): 4, (a : 1.5, b : 1.5) : 2);"
    return None
