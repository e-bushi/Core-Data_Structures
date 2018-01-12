 #!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # ...
    if base == 2:
        binary_length = len(digits)
        digit_array =[]
        decimal = 0
        for i in digits:
            if i == "0":
                digit_array.append(0)
            else:
                digit_array.append(1)

        new_digit = digit_array[::-1]
        for i in range(0, binary_length):
            if new_digit[i] == 1:
                decimal += pow(base,i)

        return(decimal)

    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    elif base == 16:
        _length = len(digits)
        hex_digits = []
        decimal = 0
        hex_alpha_value = {"a": 10, "b": 11,
        "c": 12, "d": 13, "e": 14, "f":15}

        for digit in digits:
            if digit in hex_alpha_value:
                hex_digits.append(hex_alpha_value[digit])
            else:
                hex_digits.append(int(digit))

        reversed_hex_digits = hex_digits[::-1]


        for i in range(0, _length):
            decimal += reversed_hex_digits[i] * pow(base, i)


        return decimal


    # TODO: Decode digits from any base (2 up to 36)
    # ...
    else:
        _length = len(digits)
        hex_digits = []
        decimal = 0
        char_num_val_arr = [l for l in string.ascii_lowercase]
        hex_char_val = {}

        value = 10
        for i in range(0, len(char_num_val_arr)):
            hex_char_val[char_num_val_arr[i]] = value
            value += 1


        for digit in digits:
            if digit in hex_char_val:
                hex_digits.append(hex_char_val[digit])
            else:
                hex_digits.append(int(digit))

        reversed_hex_digits = hex_digits[::-1]


        for i in range(0, _length):
            decimal += reversed_hex_digits[i] * pow(base, i)


        return decimal



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...
    exp = 0 #holds exponent value
    digit_value = 0 #keeps track of the value that will be inputted into the string
    new_base_num_string = "" # the base # string to be returned


    #determines what the largest power will be before it is larger than the number inputted
    while pow(base, exp) <= number:
        exp += 1

    #while loop stops when the exponent value is less than zero
    while exp >= 0:

        #determines if power is smaller than number, if so the value of the digit is incremented and number inputted is decremented by the power
        if pow(base, exp) <= number:
            digit_value += 1
            number -= pow(base, exp)

        #power is greater than number
        else:

            #retrieves the string ascii equivalent if the digit value is 10 or greater
            if digit_value >= 10:
                digit_value = chr(digit_value + 87)

            #adds new digit to base # string, returns digit to zero and decrements exponent value by one
            new_base_num_string += str(digit_value)
            digit_value = 0
            exp -= 1

    #checks value first element, if value is zero return string without first value
    if new_base_num_string[0] == "0":
        return new_base_num_string[1:]
    else:
        return new_base_num_string


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    #converts first base to decimal
    decimal_number = decode(digits, base1)

    #converts decimal to second base
    new_base_string = encode(decimal_number, base2)

    #return second base string
    return new_base_string


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
