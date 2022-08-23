from inputs import get_mx_size
from objects import Dimensions


def sizing(matrix_num: int) -> Dimensions:
    matrix_number: int = matrix_num
    size_matrix: Dimensions = get_mx_size(mx_number=matrix_number)
    return size_matrix


def find_summation_index(first_mx_size: Dimensions) -> int:
    return first_mx_size.stripes


def final_mx_dimension(size_mx1: Dimensions, size_mx2: Dimensions):
    stripes: int = size_mx1.lines
    lines: int = size_mx2.stripes
    return Dimensions(stripes, lines)
