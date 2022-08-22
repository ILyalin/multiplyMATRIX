from objects import Dimensions


def correct_for_multiply(size_mat1: Dimensions, size_mat2: Dimensions) -> bool:
    return size_mat1.stripes == size_mat2.lines


def correct_size(size_matrix: Dimensions) -> bool:
    print(isinstance(size_matrix.lines, int) and size_matrix.lines != 0 and isinstance(size_matrix.stripes,
                                                                                       int) and size_matrix.stripes != 0)
    return isinstance(size_matrix.lines, int) and size_matrix.lines != 0 and isinstance(size_matrix.stripes,
                                                                                        int) and size_matrix.stripes != 0


def correct_element(element: int) -> bool:
    return element != '' and isinstance(element, int)
