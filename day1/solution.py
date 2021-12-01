# import file

file = "day1/input.txt"


def ReadInput(file):
    depths_list = []
    with open(file, "r") as input:
        input_string = input.read()
        for number in input_string.split("\n"):
            depths_list.append(int(number.strip()))
    return depths_list


def CreateSlidingWindowList(depths_list):
    sliding_window_list = []
    start = 0
    stop = start + 3
    for number in depths_list:
        sliding_window_list.append(CreateMeasurementWindow(depths_list[start:stop]))
        start += 1
        stop = start + 3
    return sliding_window_list


def CreateMeasurementWindow(depths_list_slice):
    return sum(depths_list_slice)


def IsGreater(number, previous_number):
    return number > previous_number


def CheckDepthList(depths_list):
    increases = 0
    for index in range(1, len(depths_list)):
        if IsGreater(depths_list[index], depths_list[index - 1]):
            increases += 1
        else:
            pass
    return increases


if __name__ == "__main__":
    depths_list = ReadInput(file)
    result = CheckDepthList(depths_list)
    print(f"There are {result} increases.")
    sliding_window_list = CreateSlidingWindowList(depths_list)
    result = CheckDepthList(sliding_window_list)
    print(f"There are {result} sliding increases.")
