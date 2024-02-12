#region imports
import DoolittleMethod as dm
import random
import math
#endregion

#region functions
def Cholesky(Aaug):
    """
    This function finds the solution to a matrix equation Ax=b by the Colesky method
    :param Aaug: An augmented matrix
    :return: the solution vector x, L and Ltrans as a tuple
    """
    # This Function was made using ChatGPT

    # import math

    def separate_augmented(Aaug):
        A = [row[:-1] for row in Aaug]
        b = [row[-1] for row in Aaug]
        return A, b

    def cholesky_decomposition(A):
        n = len(A)
        L = [[0.0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                sum_k = sum(L[i][k] * L[j][k] for k in range(j))

                if i == j:
                    L[i][j] = math.sqrt(A[i][i] - sum_k)
                else:
                    L[i][j] = (A[i][j] - sum_k) / L[j][j]
        return L

    def forward_substitution(L, b):
        n = len(L)
        y = [0] * n
        for i in range(n):
            y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
        return y

    def backward_substitution(L, y):
        n = len(L)
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(L[j][i] * x[j] for j in range(i + 1, n))) / L[i][i]
        return x

    def Cholesky(Aaug):
        A, b = separate_augmented(Aaug)
        L = cholesky_decomposition(A)
        L_T = [list(i) for i in zip(*L)]  # Transpose of L
        y = forward_substitution(L, b)
        x = backward_substitution(L_T, y)
        return x, L, L_T

    # Example use
    Aaug = [
        [25, 15, -5, 10, 34],
        [15, 10, 1, 14, 28],
        [-5, 1, 12, -1, 14],
        [10, 14, -1, 12, 20]
    ]
    x, L, L_T = Cholesky(Aaug)
    print("Solution vector x:", x)
    print("L matrix:", L)
    print("L^T matrix:", L_T)


def SymPosDef(A):
    """
    This function first finds the transpose of A and then compares all elements of A to Atrans.
    If I pass that test, I create a vector x with random numbers and perform xtrans*A*x to see if>0.
    :param A: a nxn matrix
    :return: True if symmetric, positive definite
    """

    # #step 1:  recall that a transpose has elements such that Atrans[i][j] = A[j][i] see page 267 in MAE3013 text
    # #step 2:  check that all elements of A and Atrans are the same. if fail->return false
    # #step 3:  produce a vector x of length n filled with random floats between -1 and +1
    # #step 4:  compute xtrans*A*x
    # #step 5:  if step 4 > 0 return true else return false
    # pass

    # This Function was made using ChatGPT

    # import random
    # import math

    def transpose(A):
        n = len(A)
        Atrans = [[A[j][i] for j in range(n)] for i in range(n)]
        return Atrans

    def is_symmetric(A, Atrans):
        n = len(A)
        for i in range(n):
            for j in range(n):
                if A[i][j] != Atrans[i][j]:
                    return False
        return True

    def generate_random_vector(n):
        return [random.uniform(-1, 1) for _ in range(n)]

    def matrix_vector_product(A, x):
        n = len(A)
        result = [0] * n
        for i in range(n):
            for j in range(n):
                result[i] += A[i][j] * x[j]
        return result

    def dot_product(x, y):
        return sum(x_i * y_i for x_i, y_i in zip(x, y))

    def SymPosDef(A):
        Atrans = transpose(A)

        # Step 2: Check if A is symmetric
        if not is_symmetric(A, Atrans):
            return False

        # Step 3: Generate a random vector x
        x = generate_random_vector(len(A))

        # Step 4: Compute xtrans*A*x
        Ax = matrix_vector_product(A, x)
        xtransAx = dot_product(x, Ax)

        # Step 5: Check if result is positive
        return xtransAx > 0

    # Example
    A = [
        [2, -1, 0],
        [-1, 2, -1],
        [0, -1, 2]
    ]

    print(SymPosDef(A))


def Transpose(A):
    """
    This function finds the transpose of a square matrix
    :param A: an nxn matrix
    :return: the transpose of A
    """
    pass

def main():
    """
    Step 1:  I need to first define the matrices given in part a) of HW3_2024.
    Step 2:  pass a matrix to SymPosDef to tell if it is symmetric, positive definite
    Step 3:  based on result of Step 2, use either the Doolittle or Cholesky method to solve
    Steo 4:  check my answer by multiplying A*x to see if I get b
    Step 4:  print the solution vector and which method was used to the cli
    """
    pass
#endregion

if __name__ == "__main__":
    main()