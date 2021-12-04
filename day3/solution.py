def read_input_file(input_file):
    lines = []
    with open(input_file, "r") as f:
        input = f.read()
        for line in input.split("\n"):
            lines.append(line)
    return lines


def create_bit_columns(input_list):
    def create_column(x, input_list):
        column = []
        for input in input_list:
            column.append(input[x])
        return column

    bit_columns = {}

    for x in range(len(input_list[0])):
        bit_columns[x] = create_column(x, input_list)

    return bit_columns


def rate_calculator(bit_columns, rate_type):
    def find_more_common(column):
        if column.count("1") > column.count("0"):
            return "1"
        elif column.count("0") > column.count("1"):
            return "0"

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


def convert_list_to_string(input_list):
    return "".join(input_list)


def convert_binary_to_integer(binary_string):
    def modifier(x, binary_string):
        return int(binary_string[x]) * (2 ** int((len(binary_string) - 1) - x))

    num_list = []
    for x in range(len(binary_string)):
        num_list.append(modifier(x, binary_string))
    return sum(num_list)
