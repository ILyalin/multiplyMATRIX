def multiply(first_mx: list[list], second_mx: list[list], summ_index: int, line: int, stripe: int) -> int:
    return first_mx[line][summ_index] + second_mx[summ_index][stripe]

