# puzzle input is map of local orbits
# Except for the universal Center of Mass (COM), every object
# in space is in orbit around exactly one other object
import pdb


def parse_input_file(input_filename):
    with open(input_filename, "r") as infile:
        orbit_input = infile.read().split("\n")
        orbits = []
        for orbit in orbit_input:
            # parent is orbited by child
            parent_and_child = orbit.split(")")
            orbit = {"parent": parent_and_child[0], "child": parent_and_child[1]}
            orbits += [orbit]

    return orbits


def build_graph(orbits):
    # this is best represented as a directed graph
    # https://www.python.org/doc/essays/graphs/
    # in a directed graph, nodes are connected by arcs
    orbit_graph = {}
    for orbit in orbits:
        if orbit["parent"] not in orbit_graph.keys():
            orbit_graph[orbit["parent"]] = [orbit["child"]]
        else:
            orbit_graph[orbit["parent"]] += [orbit["child"]]
        if orbit["child"] not in orbit_graph.keys():
            orbit_graph[orbit["child"]] = []

    return orbit_graph


def cumulative_sum(n, traversed_depth=0, summation=0):
    # Base case
    if n == traversed_depth:
        return summation

    # Recursive casee
    else:
        summation += n
        n = n - 1
        return cumulative_sum(n, traversed_depth, summation)


# Global Mutable State
num_satellites = 0


def calculate_total_orbits(orbit_graph, node="COM", depth=0, traversed_depth=0):
    """
    """
    global num_satellites

    satellites = orbit_graph[node]

    # Base case: node has no child satellites
    if len(satellites) == 0:
        num_satellites += cumulative_sum(depth, traversed_depth)

    # Recursive case: node has child satellites
    else:
        for index, planet in enumerate(satellites):
            if index > 0:
                traversed_depth = depth
            calculate_total_orbits(orbit_graph, planet, depth + 1, traversed_depth)

    return num_satellites


def calculate_shortest_path(orbit_graph, planet_1, planet_2):

    return
