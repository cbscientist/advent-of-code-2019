from day_01 import fuel
from day_02 import gravityAssist
from day_03 import wires


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
    print(wire_paths)