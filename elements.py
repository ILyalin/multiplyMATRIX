from errors import element_error
from inputs import get_line_element
from objects import Dimensions
from validation import correct_element
from objects import Dimensions


def filling_elements_in_line(mx_size: Dimensions):
    line = []
    for stripe in range(int(mx_size.stripes)):
        el = get_line_element(stripe)
        while not correct_element(el):
            element_error()
            el = get_line_element(stripe)
        line.append(el)
    return line


def zero_padding_matrix(final_mx_size: Dimensions) -> list:
    final_mx = []
    for line in range(final_mx_size.lines):
        line = []
        for stripe in range(final_mx_size.stripes):
            line.append(0)
        final_mx.append(line)
    return final_mx
