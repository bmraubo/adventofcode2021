# Utility functions


def read_input_file(input_file):
    lines = []
    with open(input_file, "r") as f:
        input = f.read()
        for line in input.split("\n"):
            lines.append(line)
    return lines


def create_bit_columns(bit_rows):
    def create_column(x, input_list):
        column = []
        for input in input_list:
            column.append(input[x])
        return column

    bit_columns = {}

    for x in range(len(bit_rows[0])):
        bit_columns[x] = create_column(x, bit_rows)

    return bit_columns


def create_bit_rows(input_list):
    def create_row(string):
        row = []
        for x in range(len(string)):
            row.append(string[x])
        return row

    bit_rows = []
    for list_index in range(len(input_list)):
        bit_rows.append(create_row(input_list[list_index]))

    return bit_rows


def find_more_common(data):
    if data.count("1") > data.count("0"):
        return "1"
    elif data.count("0") > data.count("1"):
        return "0"
    elif data.count("0") == data.count("1"):
        return ""


def convert_list_to_string(input_list):
    return "".join(input_list)


def convert_string_to_list(string):
    num_list = []
    for x in string:
        num_list.append(x)
    return num_list


def convert_binary_to_integer(binary_string):
    def modifier(x, binary_string):
        return int(binary_string[x]) * (2 ** int((len(binary_string) - 1) - x))

    num_list = []
    for x in range(len(binary_string)):
        num_list.append(modifier(x, binary_string))
    return sum(num_list)


# Power Consumption Functions


def calculate_power_rate(bit_columns, rate_type):
    rate_list = power_rate_calculator(bit_columns, rate_type)
    rate_string = convert_list_to_string(rate_list)
    rate = convert_binary_to_integer(rate_string)
    return rate


def calculate_power_consumption(file):
    input = read_input_file(file)
    bit_columns = create_bit_columns(input)
    gamma_rate = calculate_power_rate(bit_columns, "gamma")
    epsilon_rate = calculate_power_rate(bit_columns, "epsilon")
    return gamma_rate * epsilon_rate


def power_rate_calculator(bit_columns, rate_type):
    def calculate_gamma_list(bit_columns):
        gamma_list = []
        for index, column in bit_columns.items():
            gamma_list.append(find_more_common(column))
        return gamma_list

    def calculate_epsilon_list(bit_columns):
        epsilon_list = []
        for index, column in bit_columns.items():
            epsilon_list.append("0" if find_more_common(column) == "1" else "1")
        return epsilon_list

    if rate_type == "gamma":
        return calculate_gamma_list(bit_columns)
    elif rate_type == "epsilon":
        return calculate_epsilon_list(bit_columns)


# Life Support Functions


def calculate_bit_criteria(bit, bit_columns, rate_type):
    def calculate_o2_rating(bit, bit_columns):
        if find_more_common(bit_columns[bit]) == "1":
            return "1"
        elif find_more_common(bit_columns[bit]) == "0":
            return "0"
        elif find_more_common(bit_columns[bit]) == "":
            print("Equal")
            return "1"

    def calculate_co2_rating(bit, bit_columns):
        if find_more_common(bit_columns[bit]) == "1":
            return "0"
        elif find_more_common(bit_columns[bit]) == "0":
            return "1"
        else:
            return "0"

    if rate_type == "O2":
        return calculate_o2_rating(bit, bit_columns)
    elif rate_type == "CO2":
        return calculate_co2_rating(bit, bit_columns)


def calculate_bit_life_support_rating(bit_rows, bit_columns, rate_type):
    def print_remaining_rows(working_list):
        print("remaining")
        for row in working_list:
            print(row)

    def print_matching_rows(working_list):
        print("matching")
        for row in working_list:
            print(row)

    remaining_columns = bit_columns
    matching_list = []
    working_list = bit_rows
    for x in range(len(bit_rows[0])):
        bit_criteria = calculate_bit_criteria(x, remaining_columns, rate_type)
        print(bit_criteria)
        for row in working_list:
            print(f"bit: {x} criteria: {bit_criteria} row: {row}")
            print_remaining_rows(working_list)
            if row[x] == bit_criteria:
                print(f"added {row}")
                print_matching_rows(matching_list)
                matching_list.append(row)
                if x == len(bit_rows[0]) - 1:
                    return convert_list_to_string(matching_list[0])
            else:
                continue
        working_list = matching_list
        matching_list = []
        remaining_columns = create_bit_columns(working_list)


def calculate_life_support_rating(bit_rows, bit_criteria):
    bit_life_support_rating_list = calculate_bit_life_support_rating(
        bit_rows, bit_criteria
    )
    life_support_rating_string = convert_list_to_string(bit_life_support_rating_list)
    life_support_rating = convert_binary_to_integer(life_support_rating_string)
    return life_support_rating


# While the x != len(bit_row[0])
# calculate bit criteria
# remove rows that do not match
# check if we have a winner

if __name__ == "__main__":
    input_file = "input.txt"
    print(calculate_power_consumption(input_file))
