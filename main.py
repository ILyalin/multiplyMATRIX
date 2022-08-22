from dimensions import final_mx_dimension
from dimensions import find_summation_index
from dimensions import sizing
from errors import element_error
from inputs import get_num_matrices, get_line_element
from messages import line_input
from multiplication import multiply
from objects import Dimensions
from validation import correct_element, correct_for_multiply


def main():
    final_matrix = []
    matrices = []
    matrices_number: int = get_num_matrices()
    matrices_dimensions: list[Dimensions] = set_mts_dimensions(mts_number=matrices_number)
    while not correct_for_multiply(size_mat1=matrices_dimensions[0], size_mat2=matrices_dimensions[1]):
        matrices_dimensions = set_mts_dimensions(mts_number=matrices_number)
    for mx_size in matrices_dimensions:
        matrix = set_mx_elements(matrix_size=mx_size, matrices_dimensions=matrices_dimensions)
        matrices.append(matrix)
    summation_index = find_summation_index(matrices_dimensions[0])
    final_mx_size = final_mx_dimension(size_mx1=matrices_dimensions[0], size_mx2=matrices_dimensions[1])
    for line in range(final_mx_size.lines):
        for stripe in range(final_mx_size.stripes):
            for index in range(summation_index):
                final_matrix[line][stripe] = multiply(first_mx=matrices[0], second_mx=matrices[1],
                                                      summ_index=summation_index, line=line, stripe=stripe)
    return final_matrix


def set_mts_dimensions(mts_number: int) -> list[Dimensions]:
    matrices_dimensions: list[Dimensions] = []
    for mx_num in range(1, mts_number + 1):
        matrix_size: Dimensions = sizing(mx_num)
        matrices_dimensions.append(matrix_size)
    return matrices_dimensions


def set_mx_elements(matrix_size: Dimensions, matrices_dimensions: list[Dimensions]) -> list[list]:
    matrix = []
    for line in range(1, matrix_size.lines + 1):
        print(line_input(line=line, matrices_dimensions=matrices_dimensions, mx_size=matrix_size))
        line = []
        for stripe in range(matrix_size.stripes):
            element = get_line_element(stripe=stripe)
            while not correct_element(element):
                print(element_error())
            line.append(element)
        matrix.append(line)
    return matrix


if __name__ == '__main__':
    main()
