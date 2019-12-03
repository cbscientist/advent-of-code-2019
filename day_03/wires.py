"""
During the rush back on Earth, the fuel management
system wasn't completely installed, so that's next on the priority
list

Front panel reveals jumble of wires

Two wires are connected to a central port and extend
outward on a grid

You trace the path each wire takes as it leaves the central
port, one wire per line of text (your puzzle input)

Wires twist and turn and occasionally cross paths

To fix the circuit, you need to find the intersection
point closest to teh central port. 

Because wires are on a grid, use the Manhattan distance
for this measurement.

Wires do technically cross right at the central point
where they both start, this point does not count, nor
does a wire count as crossing with itself.

Path is defined by direction + number of steps
R8, U5, L5, D3

First puzzle: what is the manhattan distnace
from the central port to the closest intersection?

First, need to get input"""

def parse_input_file(input_file_name):
    with open(input_file_name, 'r') as infile:
        wire_paths = infile.read().split('\n')

    wire_paths = [wire_path.split(',') for wire_path in wire_paths]

    return wire_paths