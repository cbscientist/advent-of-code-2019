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


# origin is 0,0
# r is +x
# l is -x
# u is +y
# d is -y

# Calculate the coordinates of each line segment
# wire 1, line 1, x1,y1, x2,y2, horizontal or vertical
# wire 1, line 2, x1y1 x2y2 horizontal or vertical
# wire 2, line 1, x1y1, x2y2, horizontal or vertical
# wire 2, line 2, x1y1, x2y2, horizontal or vertical

# match wire 1 horizontal with wire 2 vertical
# calculate intersection points
# calculate manhattan distance (distance from origin of 0,0)

# match wire 1 vertical with wire 2 vertical
# calculate intersection points
# calculate manhattan distance (distance from origin of 0,0)

# get list of points & manhattan distances
# find minimum manhattan distance
# return associated coordinate


def calc_manhattan_distance(point_1, point_2):
    x_distance = abs(point_2[0] - point_1[0])
    y_distance = abs(point_2[1] - point_1[1])

    return x_distance + y_distance