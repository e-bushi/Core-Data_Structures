#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests

    #returns inputted text without spaces
    altered_input_text = text.replace(" ", "")

    #loop returns inputted text with punctuation
    for c in string.punctuation:
        if c in altered_input_text:
            altered_input_text = altered_input_text.replace(c, "")

    #empty palindrome string to test
    text_reversed = ""

    #appends characters in reverse order to text_reversed variable
    for i in range(1, len(altered_input_text) + 1):
        text_reversed += altered_input_text[-i]


    #determines if reversed string is the same as the inputted altered text, if so return True - false otherwise
    if text_reversed.lower() == altered_input_text.lower():
        return True
    else:
        return False


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    #determines whether the default values are set
    if left is None and right is None:
        left = 0
        right = len(text) - 1

    #run if center is not reached
    if right > left:

        #determines if the characters in designated postions equate to a space or punctuation. If so, go to the next recursive level and iterate the next postion without comparing
        while text[left] in string.punctuation or text[left] == " ":
        # while not text[left].isalpha():
            left += 1
            # return is_palindrome_recursive(text, left, right)

        while text[right] in string.punctuation or text[right] == " ":
            right -= 1
            # return is_palindrome_recursive(text, left, right)

        #determines if characters on either side of string are the same if so return
        if text[left] == text[right]:
            right -= 1
            left += 1
            return is_palindrome_recursive(text, left, right)
        else:
            return False

    return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
