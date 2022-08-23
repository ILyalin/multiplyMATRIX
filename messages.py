def line_input(line: int, matrix_num: int) -> str:
    return f'Введите элементы {line} строки {matrix_num + 1} матрицы через Enter: '


def finished_mx_out(fin_mx: list[list]) -> str:
    final_matrix = ''
    for line in fin_mx:
        for stripe in line:
            final_matrix += str(stripe) + '|'
        final_matrix += '\n'
    return final_matrix
