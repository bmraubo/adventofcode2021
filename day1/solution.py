# import file

file = "day1/input.txt"


def ReadInput(file):
    depths_list = []
    with open(file, "r") as input:
        input_string = input.read()
        for number in input_string.split("\n"):
            depths_list.append(number.strip())
    return depths_list


def IsGreater(number, previous_number):
    return int(number) > int(previous_number)


def CheckDepthList(depths_list):
    increases = 0
    for index in range(1, len(depths_list)):
        if IsGreater(depths_list[index], depths_list[index - 1]):
            print(f"{depths_list[index]} is greater than {depths_list[index - 1]}")
            increases += 1
        else:
            print(f"{depths_list[index]} is NOT greater than {depths_list[index - 1]}")
            pass
    return increases


if __name__ == "__main__":
    depths_list = ReadInput(file)
    result = CheckDepthList(depths_list)
    print(f"There are {result} increases.")
