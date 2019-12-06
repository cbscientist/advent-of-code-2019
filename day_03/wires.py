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

import pdb

def parse_input_file(input_file_name):
    with open(input_file_name, 'r') as infile:
        wire_paths = infile.read().split('\n')

    wire_paths = [wire_path.split(',') for wire_path in wire_paths]

    return wire_paths

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

def get_coordinate_shift(direction):
    cartesian = direction[0]
    cartesian_directions = {}
    if cartesian == 'L':
        cartesian_directions['dimension'] = 'x'
        cartesian_directions['sign'] = '-'
    elif cartesian == 'R':
        cartesian_directions['dimension'] = 'x'
        cartesian_directions['sign'] = '+'
    elif cartesian == 'D':
        cartesian_directions['dimension'] = 'y'
        cartesian_directions['sign'] = '-'
    elif cartesian == 'U':
        cartesian_directions['dimension'] = 'y'
        cartesian_directions['sign'] = '+'

    magnitude = direction[1:]
    cartesian_directions['magnitude'] = magnitude

    return cartesian_directions


def calculate_line_segments(wire_path):
    position = (0,0)
    line_segments = []
    for segment in wire_path:
        x1,y1 = position
        if segment['dimension'] == 'x':
            y2 = y1
            x2 = int(segment['sign'] + segment['magnitude']) + x1
            line_type = 'horizontal'
        elif segment['dimension'] == 'y':
            x2 = x1
            y2 = int(segment['sign'] + segment['magnitude']) + y1
            line_type = 'vertical'
        position = (x2, y2)
        if x2 < x1:  # ensure proper ordering
                x = x2
                x2 = x1
                x1 = x
        if y2 < y1:
                y = y2
                y2 = y1
                y1 = y
        line_segment = [{'type': line_type, 'point_1':(x1, y1), 'point_2':(x2,y2)}]
        line_segments += line_segment

    return line_segments


def find_intersections(horizontal_segments, vertical_segments):
    intersections = []
    # pdb.set_trace()
    for horizontal_segment in horizontal_segments:
        for vertical_segment in vertical_segments:
            if horizontal_segment['point_1'][0] <= vertical_segment['point_1'][0] <= horizontal_segment['point_2'][0]:
                x_range = True
            else:
                x_range = False
            if vertical_segment['point_1'][1] <= horizontal_segment['point_1'][1] <= vertical_segment['point_2'][1]:
                y_range = True
            else:
                x_range = False

            if x_range and y_range:
                intersect = True
                intersection_point = (vertical_segment['point_1'][0], horizontal_segment['point_1'][1])
                intersections += [intersection_point]

    return intersections


def calculate_manhattan_distance(point_1, point_2=(0,0)):
    x_distance = abs(point_2[0] - point_1[0])
    y_distance = abs(point_2[1] - point_1[1])

    return x_distance + y_distance


def calculate_number_of_steps(wire_path, final_position):
    position = (0,0)
    line_segments = []
    num_steps = 0
    for segment in wire_path:
        x,y = position
        if segment['dimension'] == 'x':
            for step in range(1, int(segment['magnitude'])+1):
                x = int(segment['sign']+'1') + x
                num_steps += 1
                position = (x,y)
                if position == final_position:
                    return num_steps
        elif segment['dimension'] == 'y':
            for step in range(1, int(segment['magnitude'])+1):
                y = int(segment['sign']+'1') + y
                num_steps += 1
                position = (x,y)
                if position == final_position:
                    return num_steps
