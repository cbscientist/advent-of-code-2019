"""
Base code for the Intcode 
"""


def parse_input_file(input_file_name):
    """
    Reads in day 2 input file and
    returns a list of integers
    """
    with open(input_file_name, "r") as infile:
        integers = [int(value) for value in infile.read().split(",")]

        return integers


def initialize_values(integer_list, noun=12, verb=2):
    """
    Reads list of integers and replaces
    certain values to initialize data
    before applying IntCode processing
    """
    initialized_list = integer_list.copy()
    initialized_list[1] = noun
    initialized_list[2] = verb

    return initialized_list


def opcode_1(integer_list, processing_values, parameter_modes):
    """
    processing_values[0] == 1 should be True
    Takes the 2nd and 3rd values and adds them together
    then stores the results in the position given by the
    fourth value.
    """
    processed_list = integer_list.copy()

    if parameter_modes[-1] == 0:  # position mode
        value_1 = processed_list[processing_values[1]]
    elif parameter_modes[-1] == 1:  # immediate mode
        value_1 = processing_values[1]

    if parameter_modes[-2] == 0:
        value_2 = processing_list[processing_values[2]]
    elif parameter_modes[-2] == 1:
        value_2 = processing_values[2]

    new_value = value_1 + value_2

    processed_list[processing_values[3]] = new_value

    return processed_list


def opcode_2(integer_list, processing_values, parameter_modes):
    """
    processing_values[0] == 2 should be True
    Takes the 2nd and 3rd values and multiplies them
    together then stores the results in the positions
    given by the fourth value.
    """
    processed_list = integer_list.copy()

    if parameter_modes[-1] == 0:  # position mode
        value_1 = processed_list[processing_values[1]]
    elif parameter_modes[-1] == 1:  # immediate mode
        value_1 = processing_values[1]

    if parameter_modes[-2] == 0:
        value_2 = processing_list[processing_values[2]]
    elif parameter_modes[-2] == 1:
        value_2 = processing_values[2]
    
    new_value = value_1 * value_2

    processed_list[processing_values[3]] = new_value

    return processed_list


def opcode_3(integer_list, processing_values, parameter_modes, input_value=1):
    """
    processing_values[0] == 3 should be True
    Only has single parameter
    Takes single value as input (default to 1)
    """
    processed_list = integer_list.copy()
    processed_list[processing_values[1]] = input_value

    return processed_list


def opcode_4(integer_list, processing_values, parameter_modes):
    """
    processing_values[0] == 4 should be True
    Only has 1 parameter
    Outputs value of parameter at index given by value
    """
    return integer_list[processing_values[1]]


def intcode_processing(integer_list):
    position = 0
    intcode_list = integer_list.copy()

    while position < len(intcode_list): 
        instruction = str(intcode_list[position])
        opcode = int(instruction[-2:])
        parameter_modes = instruction[:-2]

        if opcode == 99:
            return intcode_list

        else:
            if opcode == 1:
                processing_values = intcode_list[position : position + 4]
                intcode_list = opcode_1(intcode_list, processing_values, parameter_modes)
                position += 4

            elif opcode == 2:
                processing_values = intcode_list[position : position + 4]
                intcode_list = opcode_2(intcode_list, processing_values, parameter_modes)
                position += 4

            elif opcode == 3:
                # TODO: Should take some sort of value as input
                processing_values = intcode_list[position : position + 2]
                intcode_list = opcode_3(intcode_list, processing_values, parameter_modes)
                position += 2

            elif opcode == 4:
                processing_values = intcode_list[position : position + 2]
                intcode_list = opcode_4(intcode_list, processing_values, parameter_modes)
                position += 2


def get_initial_values(integer_list, output=19690720):
    for noun in range(100):  # 99 + 1
        for verb in range(100):
            intcode_to_test = initialize_values(integer_list, noun, verb)
            processed_list = intcode_processing(intcode_to_test)
            print("Tried {}, {}".format(noun, verb))
            if processed_list[0] == output:
                return (noun, verb)
            else:
                pass


def calculate_day2_output(noun, verb):
    return 100 * noun + verb
