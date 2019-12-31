from math import floor


def parse_input_file(input_file_name):
    """
    Reads in day 1 input file and 
    returns list of masses represented
    as integers
    """
    with open(input_file_name, "r") as infile:
        masses = [int(mass) for mass in infile.read().split("\n")]

    return masses


def calculate_fuel(module_mass):
    """
    Takes as input a module mass and returns
    the fuel needed to launch the module.
    """
    module_fuel = floor(module_mass / 3) - 2
    return module_fuel


def calculate_total_fuel(cumulative_fuel):
    additional_fuel_needed = calculate_fuel(cumulative_fuel)

    if additional_fuel_needed <= 0:
        print(cumulative_fuel)
        return cumulative_fuel

    else:
        additional_mass = additional_fuel_needed
        print(cumulative_fuel)
        return cumulative_fuel + calculate_total_fuel(additional_mass)
