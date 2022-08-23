from dimensions import final_mx_dimension
from dimensions import find_summation_index
from elements import zero_padding_matrix
from errors import muliply_error
from inputs import get_num_matrices
from multiplication import multiply
from objects import Dimensions
from settings import set_mts_dimensions, set_mx_elements
from validation import correct_for_multiply
from messages import finished_mx_out


def main():
    final_matrix = []
    matrices = []
    matrices_number: int = get_num_matrices()
    matrices_dimensions: list[Dimensions] = set_mts_dimensions(mts_number=matrices_number)
    f = True
    while f:
        if correct_for_multiply(size_mat1=matrices_dimensions[0], size_mat2=matrices_dimensions[1]):
            for mx_size in matrices_dimensions:
                matrix = set_mx_elements(matrix_num=matrices_dimensions.index(mx_size), matrix_size=mx_size)
                matrices.append(matrix)
            summation_index = find_summation_index(matrices_dimensions[0])
            final_mx_size = final_mx_dimension(size_mx1=matrices_dimensions[0], size_mx2=matrices_dimensions[1])
            final_matrix = zero_padding_matrix(final_mx_size)
            for line in range(final_mx_size.lines):
                for stripe in range(final_mx_size.stripes):
                    element = 0
                    for index in range(summation_index):
                        element += multiply(first_mx=matrices[0], second_mx=matrices[1], summ_index=index, line=line,
                                            stripe=stripe)
                        f = False
                    final_matrix[line][stripe] = element
        else:
            print(muliply_error())
            matrices_dimensions: list[Dimensions] = set_mts_dimensions(mts_number=matrices_number)
    return final_matrix


if __name__ == '__main__':
    matrix_out = finished_mx_out(main())
    print(matrix_out)

