"""
Intcode program

Ship's computer has burst into flames

Intcode program is a list of integers separated by commas

First integer is opcode

Opcode 1 adds together numbers read from two positions
and stores in the result in a third position

First two integers immediately after the opcode indicate
the positions from which you should read the input values

Third indicates the position at which the output should
be stored

Opcode 2 works exactly like opcode 1, except that it
multiples the two values together instead of adding them

Once you're done with an opcode, process the next one
by moving forward 4 positions

First step is to restore the computer to the state
it was in before it burst into flames, and was just
giving you an error

before running program, replace position 1 with value 12
and replace position 2 with value 2

0 indexed

ok - I think this is enough notes for now, jeez
"""

def parse_input_file(input_file_name):
    """
    Reads in day 2 input file and
    returns a list of integers
    """
    with open(input_file_name, 'r') as infile:
        integers = [int(value) for value in infile.read().split(',')]

        return integers


def initialize_values(integer_list, noun=12, verb=2):
    """
    Reads list of integers and replaces
    certain values to initialize data
    before applying IntCode processing
    """
    initialized_list = integer_list
    initialized_list[1] = noun
    initialized_list[2] = verb

    return initialized_list


def opcode_1(integer_list, processing_values):
    processed_list = integer_list
    value_1 = integer_list[processing_values[1]]
    value_2 = integer_list[processing_values[2]]

    new_value = value_1 + value_2

    processed_list[processing_values[3]] = new_value

    return processed_list


def opcode_2(integer_list, processing_values):
    processed_list = integer_list
    value_1 = processed_list[processing_values[1]]
    value_2 = processed_list[processing_values[2]]

    new_value = value_1 * value_2

    processed_list[processing_values[3]] = new_value

    return processed_list


def intcode_processing(integer_list):
    position = 0
    intcode_list = integer_list

    while position < len(intcode_list):
        opcode = intcode_list[position]
        
        if opcode == 99:
            return intcode_list

        else:
            processing_values = intcode_list[position:position+4]

            if opcode == 1:
                intcode_list = opcode_1(intcode_list, processing_values)
                position += 4

            elif opcode == 2:
                intcode_list = opcode_2(intcode_list, processing_values)
                position += 4


# To complete the gravity assist you need to determine what pair of inputs
# produces the output 19690720


def get_initial_values(integer_list, output=19690720):
    for noun in range(100):  # 99 + 1
        for verb in range(100):
            print(noun, verb)
            print(integer_list)
            temp_list = initialize_values(integer_list, noun, verb)
            print(temp_list)
            processed_list = intcode_processing(temp_list)
            print("Tried {}, {}".format(noun, verb))
            if processed_list[0] == output:
                return (noun, verb)
            else:
                pass









