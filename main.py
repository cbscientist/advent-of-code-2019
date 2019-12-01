from day_01 import fuel


if __name__=="__main__":
    masses = fuel.parse_input_file('day_01/input.txt')
    fuel_needed = sum([fuel.calculate_total_fuel(fuel.calculate_fuel(mass)) for mass in masses])

    print("This is the amount of fuel needed: {}".format(fuel_needed))