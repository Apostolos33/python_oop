def print_apper_part(size):
    for row in range(1, size):
        print(" " * (size - row) + "* " * row)

def print_lower_part(size):
    for row in range(size, 0, -1):
        print(" " * (size - row) + "* " * row)

def rhombus(size):
    print_apper_part(size)
    print_lower_part(size)

number = int(input())
rhombus(number)