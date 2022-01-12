def compute_distance(obj1, obj2):
    if isinstance(obj1, Node) and isinstance(obj2, Node):
        return obj1.distances[obj1.index][obj2.index]
    if isinstance(obj1, Tree) and isinstance(obj2, Node):
        left_distance = obj1.left_branch.compute_distance(obj2)
        right_distance = obj1.right_branch.compute_distance(obj2)
        total_distance = (left_distance + right_distance) / 2
        return total_distance
    if isinstance(obj1, Node) and isinstance(obj2, Tree):
        left_distance = obj2.left_branch.compute_distance(obj1)
        right_distance = obj2.right_branch.compute_distance(obj1)
        total_distance = (left_distance + right_distance) / 2
        return total_distance
    if isinstance(obj1, Tree) and isinstance(obj2, Tree):
        left_distance = obj1.compute_distance(obj2.left_branch)
        right_distance = obj1.right_branch.compute_distance(obj2.right_branch)
        total_distance = (left_distance + right_distance) / 2
        return total_distance

class Node:
    def __init__(self, node_name, distance_info):
        self.node_name = node_name
        self.distance_info = distance_info
        self.distances = distance_info[0]
        self.names = distance_info[1]
        self.index = self.names.index(node_name)

    def get_nodes(self):
        return [self.node_name]

    def compute_distance(self, other):
        if isinstance(other, Node):
            return self.distances[self.index][other.index]
        elif isinstance(other, Tree):
            return other.compute_distance(self)
        else:
            raise TypeError("Only supported between trees and nodes")

    def __add__(self, other):
        if isinstance(other, Node):
            half_distance = self.compute_distance(other)/2
            return Tree(self, half_distance, other, half_distance, self.distance_info)
        elif isinstance(other, Tree):
            return other + self
        else:
            raise TypeError("Only supported between trees and nodes")


class Tree:
    def __init__(self, left_branch, left_branch_distance, right_branch, right_branch_distance, distance_info):
        self.left_branch = left_branch
        self.left_branch_distance = left_branch_distance
        self.right_branch = right_branch
        self.right_branch_distance = right_branch_distance
        self.distance_info = distance_info

    def __add__(self, other):
        if not isinstance(other, Tree):
            if not isinstance(other, Node):
                raise TypeError("Only supported between trees and nodes")

        if isinstance(other, Node)

    def __repr__(self):
        pass

    def compute_distance(self, other):
        if not isinstance(other, Tree):
            if not isinstance(other, Node):
                raise TypeError("Only supported between trees and nodes")

        if isinstance(other, Node):
            left_distance = self.left_branch.compute_distance(other)
            right_distance = self.right_branch.compute_distance(other)
            total_distance = (left_distance + right_distance) / 2
            return total_distance

        if isinstance(other, Tree):
            left_distance = self.compute_distance(other.left_branch)
            right_distance = self.right_branch.compute_distance(other.right_branch)
            total_distance = (left_distance + right_distance) / 2
            return total_distance






def main():
    matrix_dist = [[0, 3, 12, 12, 10], [3, 0, 13, 13, 10], [12, 3, 0, 6, 7], [12, 13, 6, 0, 7], [9, 10, 7, 7, 0]]
    nodes = ["a", "b", "c", "d", "e"]
    distance_info = matrix_dist, nodes


