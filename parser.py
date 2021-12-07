
def autoparse(input_file):
    input = open(input_file, "r")
    exit = False
    output = []
    for line in input:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        output.append(line_list)
    return output

def singleparse(input_file):
    input = open(input_file)
    return input.read().splitlines()

def commaparse(input_file):
    input = open(input_file)
    return input.read().split(",")


        