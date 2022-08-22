from errors import element_error
from inputs import get_line_element
from objects import Dimensions
from validation import correct_element


def filling_elements_in_line(mx_size: Dimensions):
    line = []
    for stripe in range(int(mx_size.stripes)):
        el = get_line_element(stripe)
        while not correct_element(el):
            element_error()
            el = get_line_element(stripe)
        line.append(el)
    return line
