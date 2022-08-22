from objects import Dimensions
from errors import size_error


def get_mx_size(mx_number: int) -> Dimensions:
    f = True
    while f:
        try:
            lines, stripes = map(int, input(f'Введите размеры {mx_number} матрицы через знак "|": ').split('|'))
            return Dimensions(lines, stripes)

        except ValueError:
            print(size_error())


def get_num_matrices() -> int:
    return int(input('Введите кол-во матриц в произведении: '))


def get_line_element(stripe: int) -> int:
    return int(input(f'{stripe + 1}. '))
