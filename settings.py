from dimensions import sizing
from elements import filling_elements_in_line
from messages import line_input
from objects import Dimensions


def set_mts_dimensions(mts_number: int) -> list[Dimensions]:
    matrices_dimensions: list[Dimensions] = []
    for mx_num in range(1, mts_number + 1):
        matrix_size: Dimensions = sizing(mx_num)
        matrices_dimensions.append(matrix_size)
    return matrices_dimensions


def set_mx_elements(matrix_num: int, matrix_size: Dimensions) -> list[list]:
    matrix = []
    for line in range(1, matrix_size.lines + 1):
        print(line_input(line=line, matrix_num=matrix_num))
        line = filling_elements_in_line(mx_size=matrix_size)
        matrix.append(line)
    return matrix
