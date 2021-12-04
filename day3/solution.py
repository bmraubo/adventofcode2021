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


def find_most_common(bit_columns):
    def count_bits(column):
        if column.count("1") > column.count("0"):
            return "1"
        elif column.count("0") > column.count("1"):
            return "0"

    gamma_list = []
    for index, column in bit_columns.items():
        gamma_list.append(count_bits(column))

    return gamma_list


def convert_list_to_string(input_list):
    return "".join(input_list)
