#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)
    return factorial_iterative(n)


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    factorial_product = n
    iterations = n - 1

    #factorial(0) will always equate to 1
    if n == 0:
        return 1


    while iterations > 0:
        #factorial product times its immediate descendant number
        factorial_product *= (n - 1)

        #decrement iteration to prevent infinite loop
        iterations -= 1

        #decrement number to make sure factorial_product wont be mulitiplied by itself
        n -= 1

    return factorial_product
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests


def factorial_recursive(n):
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
