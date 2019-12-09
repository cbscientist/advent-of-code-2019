# puzzle input is map of local orbits
# Except for the universal Center of Mass (COM), every object
# in space is in orbit around exactly one other object
import pdb

def parse_input_file(input_filename):
    with open(input_filename, 'r') as infile:
        orbit_input = infile.read().split('\n')
        orbits = []
        for orbit in orbit_input:
            # parent is orbited by child
            parent_and_child = orbit.split(')')
            orbit = {'parent': parent_and_child[0],'child': parent_and_child[1]}
            orbits += [orbit]

    return orbits


def build_graph(orbits):
    # this is best represented as a directed graph
    # https://www.python.org/doc/essays/graphs/
    # in a directed graph, nodes are connected by arcs
    orbit_graph = {}
    for orbit in orbits:
        if orbit['parent'] not in orbit_graph.keys():
            orbit_graph[orbit['parent']] = [orbit['child']]
        else:
            orbit_graph[orbit['parent']] += [orbit['child']]
        if orbit['child'] not in orbit_graph.keys():
            orbit_graph[orbit['child']] = []

    return orbit_graph


def calculate_total_orbits(orbit_graph, node='COM', num_satellites=0):  #orbit_graph.keys()

    # pdb.set_trace()
    if orbit_graph[node] != []:
        for satellite in orbit_graph[node]:
            num_satellites += 1
            additional_satellites = calculate_total_orbits(orbit_graph, satellite, num_satellites)
            print("Node: {}, num_satellites:{}".format(node, num_satellites))
            return additional_satellites
            
    else:
        print("Node: {}, num_satellites:{}".format(node, 0))
        return 1

