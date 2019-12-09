from day_01 import fuel
from day_02 import gravityAssist
from day_03 import wires
from day_06 import orbit

import pdb


if __name__=="__main__":

    # # Day 1 Processing
    # masses = fuel.parse_input_file('day_01/input.txt')
    # fuel_needed = sum([fuel.calculate_total_fuel(fuel.calculate_fuel(mass)) for mass in masses])

    # print("This is the amount of fuel needed: {}".format(fuel_needed))

    # # Day 2 Processing
    # integers = gravityAssist.parse_input_file('day_02/input.txt')
    # new_integers = gravityAssist.initialize_values(integers)
    # final_integers = gravityAssist.intcode_processing(new_integers)

    # print("This is position 0 of the final integer list:{}".format(final_integers[0]))

    # integers = gravityAssist.parse_input_file('day_02/input.txt')
    # noun, verb = gravityAssist.get_initial_values(integers)
    # solution_input = gravityAssist.calculate_day2_output(noun, verb)

    # print("The noun is {} and the verb is {}".format(noun, verb))
    # print("The value to submit as your answer is {}".format(solution_input))

    # Day 3 Processing

    wire_paths = wires.parse_input_file('day_03/input.txt')
    wire_path_1 = wire_paths[0]
    wire_path_2 = wire_paths[1]

    # wire_path_1 = ['R8','U5','L5','D3']
    # wire_path_2 = ['U7','R6','D4','L4']

    # wire_path_1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    # wire_path_2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

    # wire_path_1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
    # wire_path_2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

    # shifts_1 = []
    # for direction in wire_path_1:
    #     shift = wires.get_coordinate_shift(direction)
    #     shifts_1 += [shift]

    # shifts_2 = []
    # for direction in wire_path_2:
    #     shift = wires.get_coordinate_shift(direction)
    #     shifts_2 += [shift]

    # line_segments_1 = wires.calculate_line_segments(shifts_1)
    # horizontal_line_segments_1 = [segment for segment in line_segments_1 if segment['type']=='horizontal']
    # vertical_line_segments_1 = [segment for segment in line_segments_1 if segment['type']=='vertical']

    # line_segments_2 = wires.calculate_line_segments(shifts_2)
    # horizontal_line_segments_2 = [segment for segment in line_segments_2 if segment['type']=='horizontal']
    # vertical_line_segments_2 = [segment for segment in line_segments_2 if segment['type']=='vertical']

    # intersections_1 = wires.find_intersections(horizontal_line_segments_1, vertical_line_segments_2)
    # intersections_2 = wires.find_intersections(horizontal_line_segments_2, vertical_line_segments_1)

    # all_intersections = intersections_1 + intersections_2
    # distances = []
    # for intersection in all_intersections:
    #     if intersection != (0,0):
    #         distance = wires.calculate_manhattan_distance(intersection)
    #         distances += [{'intersection': intersection, 'distance':distance}]


    # min_distance = min([intersection['distance'] for intersection in distances])
    # final_coordinate = [intersection['intersection'] for intersection in distances if intersection['distance'] == min_distance][0]

    # all_combined_steps = []
    # for intersection in all_intersections:
    #     if intersection != (0,0):
    #         num_steps_1 = wires.calculate_number_of_steps(shifts_1, intersection)
    #         num_steps_2 = wires.calculate_number_of_steps(shifts_2, intersection)
    #         combined_steps = num_steps_1 + num_steps_2
    #         all_combined_steps += [combined_steps]

    # print(min(all_combined_steps))
    # pdb.set_trace()

    orbits = orbit.parse_input_file('day_06/test_input.txt')

    orbit_graph = orbit.build_graph(orbits)
    print(orbit_graph)

    total = orbit.calculate_total_orbits(orbit_graph)
    print(total)


    


    
