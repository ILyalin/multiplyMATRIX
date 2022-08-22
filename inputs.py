from objects import Dimensions
from validation import correct_size


def get_mx_size(mx_number: int) -> Dimensions:
    lines, stripes = input(f'Введите размеры {mx_number} матрицы через знак "|": ').split('|')
    return Dimensions(lines, stripes)


def get_num_matrices() -> int:
    return int(input('Введите кол-во матриц в произведении: '))


def get_line_element(stripe: int) -> int:
    return int(input(f'{stripe + 1}. '))
