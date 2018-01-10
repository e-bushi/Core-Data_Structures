
import string

def decode(digits, base):
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




print(decode("101110", 4))
