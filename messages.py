from objects import Dimensions


def line_input(line: int, matrices_dimensions: list[Dimensions], mx_size:Dimensions) -> str:
    return f'Введите элементы {line} строки {matrices_dimensions.index(mx_size) + 1} матрицы через Enter: '
