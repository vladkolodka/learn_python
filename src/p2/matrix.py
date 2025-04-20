from typing import Callable, Any

class Matrix:
    def __init__(self, rows: int, cols: int, value_gen: Callable[[int, int], Any]):
        self.rows = rows
        self.cols = cols
        self.data = [[value_gen(i, j) for j in range(cols)] for i in range(rows)]

    def __getitem__(self, index):
        return self.data[index]

    def transpose(self):
        return Matrix(self.cols, self.rows, lambda i, j: self.data[j][i])

    def __repr__(self):
        border = "+" + "-" * (len(self.data[0]) * 5 - 1) + "+"
        result = [border]
        for row in self.data:
            result.append("| " + " | ".join(str(cell).rjust(2) for cell in row) + " |")
        result.append(border)
        return "\n".join(result)

    def multiply_matrix(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.rows, other.cols, lambda i, j: sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)))
        else:
            raise ValueError("Cannot multiply matrix with non-matrix type.")

    def __mul__(self, other: 'Matrix'):
        return self.multiply_matrix(other)


def def_matrix(x: int, y: int, value_gen: Callable[[int, int], Any]) -> list[list[Any]]:
    return [[value_gen(i, j) for i in range(x)] for j in range(y)]

def transpose(matrix: list[list[Any]]) -> list[list[Any]]:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def multiply_matrix(matrix_a: list[list[Any]], matrix_b: list[list[Any]]) -> list[list[Any]]:
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Cannot multiply matrices with incompatible dimensions.")

    result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def print_matrix(matrix):
    border = "+" + "-" * (len(matrix[0]) * 5 - 1) + "+"
    print(border)
    for row in matrix:
        print("| " + " | ".join(str(cell).rjust(2) for cell in row) + " |")
    print(border)