file = "day2/input.txt"


def ReadInput(file):
    def ConvertToTuple(instruction):
        direction = instruction.split()[0]
        value = instruction.split()[1]
        return (direction, int(value))

    instructions = []
    with open(file, "r") as input:
        input_string = input.read()
        for instruction in input_string.split("\n"):
            instructions.append(ConvertToTuple(instruction))
    return instructions


def CalculateLocation(instructions):
    horizontal_position = 0
    aim = 0
    depth = 0

    for direction, value in instructions:
        if direction == "forward":
            horizontal_position += value
            depth += value * aim
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    return (horizontal_position, depth)


def Multiply(location):
    return location[0] * location[1]


if __name__ == "__main__":
    instructions = ReadInput(file)
    location = CalculateLocation(instructions)
    print(Multiply(location))
