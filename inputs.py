from objects import Dimensions
from errors import size_error, element_error, mx_number_error


def get_mx_size(mx_number: int) -> Dimensions:
    f = True
    while f:
        try:
            lines, stripes = map(int, input(f'Введите размеры {mx_number} матрицы через знак "|": ').split('|'))
            return Dimensions(lines, stripes)

        except ValueError:
            print(size_error())


def get_num_matrices() -> int:
    f = True
    while f:
        try:
            return int(input('Введите кол-во матриц в произведении: '))
        except ValueError:
            print(mx_number_error())
            return int(input('Введите кол-во матриц в произведении: '))


def get_line_element(stripe: int) -> int:
    f = True
    while f:
        try:
            return int(input(f'{stripe + 1}. '))
        except ValueError:
            print(element_error())
            return int(input(f'{stripe + 1}. '))
