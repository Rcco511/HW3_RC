# Ross Compston
# Homework Week 3
# Made with the assistance of chatgpt

from math import sqrt, exp, pi

def t_distribution_pdf(x, nu):
    """
    Approximates the PDF of the t-distribution for a given value x and degrees of freedom nu.

    :param x: The variable value at which the PDF is evaluated.
    :param nu: Degrees of freedom of the t-distribution.
    :return: The PDF value at x.
    """
    return (1.0 / sqrt(nu)) * (1 + x ** 2 / nu) ** (-((nu + 1.0) / 2))


def Simpson(fcn, nu, a, b, npoints=100):
    """
    Numerically integrates a function using the Simpson's rule.

    :param fcn: The function to be integrated.
    :param nu: The degrees of freedom, passed to the function.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param npoints: The number of points to use in the approximation.
    :return: The approximate integral of the function from a to b.
    """
    if npoints % 2 == 1: npoints += 1
    h = (b - a) / npoints
    s = fcn(a, nu) + fcn(b, nu)
    for i in range(1, npoints, 2):
        s += 4 * fcn(a + i * h, nu)
    for i in range(2, npoints - 1, 2):
        s += 2 * fcn(a + i * h, nu)
    return s * h / 3


def calculate_cdf_upper_limit(nu, upper_limit):
    """
    Calculates the cumulative distribution function (CDF) up to an upper limit for the t-distribution.

    :param nu: Degrees of freedom for the t-distribution.
    :param upper_limit: The upper limit up to which to calculate the CDF.
    :return: The CDF value up to the upper limit.
    """
    a = -5 * sqrt(nu)  # Start from a value sufficiently far from the mean
    b = upper_limit
    cdf = Simpson(t_distribution_pdf, nu, a, b)
    return cdf


def main():
    """
    Main function to prompt user input for calculating the CDF of the t-distribution
    and allow restarting the calculation.
    """
    while True:
        nu = int(input("Enter the degrees of freedom (integer): "))
        upper_limit = float(input("Enter the upper integration limit (float): "))

        cdf_upper_limit = calculate_cdf_upper_limit(nu, upper_limit)
        print(f"F({upper_limit}) = {cdf_upper_limit:.4f}")

        restart = input("Do you want to start over? (y/n): ").strip().lower()
        if restart != "y":
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()






# region old
# #region imports
# from hw2a import Simpson
# from math import sqrt, exp, pi
# #endregion
#
#
# def t_distribution_pdf(x, nu):
#     return (1.0 / sqrt(nu)) * (1 + x ** 2 / nu) ** (-((nu + 1.0) / 2))
#
#
# def Simpson(fcn, nu, a, b, npoints=100):
#     if npoints % 2 == 1: npoints += 1
#     h = (b - a) / npoints
#     s = fcn(a, nu) + fcn(b, nu)
#     for i in range(1, npoints, 2):
#         s += 4 * fcn(a + i * h, nu)
#     for i in range(2, npoints - 1, 2):
#         s += 2 * fcn(a + i * h, nu)
#     return s * h / 3
#
#
# def calculate_cdf_upper_limit(nu, upper_limit):
#     a = -5 * sqrt(nu)
#     b = upper_limit
#     cdf = Simpson(t_distribution_pdf, nu, a, b)
#     return cdf
#
#
# def main():
#     while True:
#         nu = int(input("Enter the degrees of freedom (integer): "))
#         upper_limit = float(input("Enter the upper integration limit (float): "))
#
#         cdf_upper_limit = calculate_cdf_upper_limit(nu, upper_limit)
#         print(f"F({upper_limit}) = {cdf_upper_limit:.4f}")
#
#         restart = input("Do you want to start over? (y/n): ").strip().lower()
#         if restart != "y":
#             print("Exiting program.")
#             break
#
#
# if __name__ == "__main__":
#     main()
# endregion
