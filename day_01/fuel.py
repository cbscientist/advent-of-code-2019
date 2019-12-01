from math import floor


def parse_input_file(input_file_name):
    """
    Reads in day 1 input file and 
    returns list of masses represented
    as integers
    """
    with open(input_file_name, 'r') as infile:
        masses = [int(mass) for mass in infile.read().split('\n')]

    return masses


def calculate_fuel(module_mass):
    """
    Takes as input a module mass and returns
    the fuel needed to launch the module.
    """
    module_fuel = floor(module_mass / 3) - 2
    return module_fuel