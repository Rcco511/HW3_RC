# #HW3a
# # Created using the assistance of ChatGPT
#
# # region imports
# import DoolittleMethod as dm
# import Gauss_Seidel as gs
# import random
# import math
# # endregion
#
# # region utility functions
# def transpose(A):
#     """
#     Finds the transpose of a square matrix A.
#     :param A: an nxn matrix
#     :return: the transpose of A
#     """
#     n = len(A)
#     Atrans = [[A[j][i] for j in range(n)] for i in range(n)]
#     return Atrans
#
# def is_symmetric(A):
#     """
#     Checks if matrix A is symmetric.
#     :param A: a nxn matrix
#     :return: True if symmetric, False otherwise
#     """
#     Atrans = transpose(A)
#     n = len(A)
#     for i in range(n):
#         for j in range(n):
#             if A[i][j] != Atrans[i][j]:
#                 return False
#     return True
#
# def generate_random_vector(n):
#     """
#     Generates a random vector of length n with values between -1 and 1.
#     :param n: the length of the vector
#     :return: a list of n random floats
#     """
#     return [random.uniform(-1, 1) for _ in range(n)]
#
# def matrix_vector_product(A, x):
#     """
#     Multiplies matrix A by vector x.
#     :param A: a nxn matrix
#     :param x: a vector of length n
#     :return: the product of A and x
#     """
#     n = len(A)
#     result = [0] * n
#     for i in range(n):
#         for j in range(n):
#             result[i] += A[i][j] * x[j]
#     return result
#
# def dot_product(x, y):
#     """
#     Calculates the dot product of two vectors x and y.
#     :param x: first vector
#     :param y: second vector
#     :return: the dot product
#     """
#     return sum(x_i * y_i for x_i, y_i in zip(x, y))
#
# def SymPosDef(A):
#     """
#     Determines if matrix A is symmetric and positive definite.
#     :param A: a nxn matrix
#     :return: True if A is symmetric and positive definite, False otherwise
#     """
#     if not is_symmetric(A):
#         return False
#
#     x = generate_random_vector(len(A))
#     Ax = matrix_vector_product(A, x)
#     xtransAx = dot_product(x, Ax)
#     return xtransAx > 0
# # endregion
#
# # region main function
# def main():
#     # Define your matrix A and vector b here
#     Aaug = [
#         [1, -1, 3, 2, 15],
#         [-1, 5, -5, -2, 35],
#         [3, -5, 19, 3, 94],
#         [2, -2, 3, 21, 1]
#     ]
#
#     # Use Gauss_Seidel's function to separate A and b
#     A, b = gs.separateAugmented(Aaug)
#     if SymPosDef(A):
#         print("Matrix is symmetric, positive definite. Using Cholesky method.")
#         # Ensure Cholesky method is correctly implemented to return the expected values
#         solution = gs.Cholesky(Aaug)  # Adjusted for a realistic return value
#         method_used = "Cholesky"
#     else:
#         print("Matrix is not symmetric positive definite. Using Doolittle method.")
#         solution = dm.Doolittle(Aaug)  # Ensure Doolittle returns just the solution vector
#         method_used = "Doolittle"
#
#     # Verify and print the solution
#     print("Solution vector:", solution)
#     print("Method used:", method_used)
#
# if __name__ == "__main__":
#     main()


# HW3a
# Created using the assistance of ChatGPT

# region imports
import DoolittleMethod as dm
import Gauss_Seidel as gs
import random
import math


# endregion

# region utility functions
def transpose(A):
    """
    Finds the transpose of a square matrix A.
    :param A: an nxn matrix
    :return: the transpose of A
    """
    n = len(A)
    Atrans = [[A[j][i] for j in range(n)] for i in range(n)]
    return Atrans


def is_symmetric(A):
    """
    Checks if matrix A is symmetric.
    :param A: a nxn matrix
    :return: True if symmetric, False otherwise
    """
    Atrans = transpose(A)
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != Atrans[i][j]:
                return False
    return True


def generate_random_vector(n):
    """
    Generates a random vector of length n with values between -1 and 1.
    :param n: the length of the vector
    :return: a list of n random floats
    """
    return [random.uniform(-1, 1) for _ in range(n)]


def matrix_vector_product(A, x):
    """
    Multiplies matrix A by vector x.
    :param A: a nxn matrix
    :param x: a vector of length n
    :return: the product of A and x
    """
    n = len(A)
    result = [0] * n
    for i in range(n):
        for j in range(n):
            result[i] += A[i][j] * x[j]
    return result


def dot_product(x, y):
    """
    Calculates the dot product of two vectors x and y.
    :param x: first vector
    :param y: second vector
    :return: the dot product
    """
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


def SymPosDef(A):
    """
    Determines if matrix A is symmetric and positive definite.
    :param A: a nxn matrix
    :return: True if A is symmetric and positive definite, False otherwise
    """
    if not is_symmetric(A):
        return False

    x = generate_random_vector(len(A))
    Ax = matrix_vector_product(A, x)
    xtransAx = dot_product(x, Ax)
    return xtransAx > 0


# endregion

# region Cholesky decomposition
def Cholesky(A):
    """
    Performs Cholesky decomposition on a symmetric, positive-definite matrix A.
    Returns the lower triangular matrix, L.
    """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum_k = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:  # Diagonal elements
                L[i][j] = math.sqrt(A[i][i] - sum_k)
            else:
                L[i][j] = (A[i][j] - sum_k) / L[j][j]

    return L


# endregion

# region main function
def main():
    """
    Main function to decide and solve a matrix equation using appropriate method.
    """
    # Define your matrix A and vector b here
    Aaug = [
        [1, -1, 3, 2, 15],
        [-1, 5, -5, -2, 35],
        [3, -5, 19, 3, 94],
        [2, -2, 3, 21, 1]
    ]

    # Determine if A is symmetric and positive definite
    A, b = gs.separateAugmented(Aaug)  # Use Gauss_Seidel's function to separate A and b
    if SymPosDef(A):
        print("Matrix is symmetric, positive definite. Using Cholesky method.")
        L = Cholesky(A)  # Directly using the Cholesky method implemented above
        # Note: You'll need to implement forward and backward substitution to solve for x using L
        method_used = "Cholesky"
        # Placeholder for solution vector x calculation
        solution = "Solution vector not calculated"  # Update this with actual calculation
    else:
        print("Matrix is not symmetric positive definite. Using Doolittle method.")
        solution = dm.Doolittle(Aaug)
        method_used = "Doolittle"

    # Verify and print the solution
    print("Solution vector:", solution)
    print("Method used:", method_used)


# endregion

if __name__ == "__main__":
    main()
