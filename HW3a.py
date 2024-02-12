#region imports
import DoolittleMethod as dm
#endregion

#region functions
def Cholesky(Aaug):
    """
    This function finds the solution to a matrix equation Ax=b by the Colesky method
    :param Aaug: An augmented matrix
    :return: the solution vector x, L and Ltrans as a tuple
    """
    #step 1:  split the Aaug into A and b (see separateAugmented in Gauss_Seidel.py)
    #step 2:  factor into L and Ltrans according to Cholesky formulae
    #step 3:  use backsolving to find x (see methods in DoolittleMethod.py)
    #step 4:  return (x,L,Ltrans)
    pass

def SymPosDef(A):
    """
    This function first finds the transpose of A and then compares all elements of A to Atrans.
    If I pass that test, I create a vector x with random numbers and perform xtrans*A*x to see if>0.
    :param A: a nxn matrix
    :return: True if symmetric, positive definite
    """
    #step 1:  recall that a transpose has elements such that Atrans[i][j] = A[j][i] see page 267 in MAE3013 text
    #step 2:  check that all elements of A and Atrans are the same. if fail->return false
    #step 3:  produce a vector x of length n filled with random floats between -1 and +1
    #step 4:  compute xtrans*A*x
    #step 5:  if step 4 > 0 return true else return false
    pass

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