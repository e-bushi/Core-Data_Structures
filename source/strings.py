#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    index_of_pattern = 0

    #the largest index
    pattern_index_length = len(pattern)

    #the length of the patterns
    pattern_length = len(pattern)

    #index of text
    index = 0

    #the number of overall matches
    matches = 0

    #the indices of the matches
    array_of_matches_indices = []

    #temporary array to hold the matching indices
    temp_array_of_matches = []

    #determines if pattern is an empty string if so
    #return True
    if pattern == '':
        return True

    #loop condition that defines whether the index of the text has reached the length of the text
    while index < len(text):

        #condition to check if the pattern and the text share the same character at the designated index
        if pattern[index_of_pattern] == text[index]:
            temp_array_of_matches.append(index)

            index_of_pattern += 1
            index += 1
            matches += 1

            #determines if the number of matches equates to the number of characters in the pattern than we'll move the indices stored within the temp array to the permanent array
            if matches == pattern_length:
                array_of_matches_indices.extend(temp_array_of_matches)
                matches = 0
                index_of_pattern = 0

            #determines if the index exceed the actual length of the text
            if index == len(text):
                break

        #in the case of the characters not matching we revert the pattern back to the first character, reset the number of matches and clear the temp array
        if pattern[index_of_pattern] != text[index]:
            index_of_pattern = 0
            matches = 0
            temp_array_of_matches = []

            #if after the changes above we the two characters don't equate then we will go to the next character within the text to compare
            if pattern[index_of_pattern] != text[index]:
                index += 1


    #determines if the length of the array is greater than zero and if the number of indices within the array exceeds the number of characters in a pattern, that the number of elements in the array are divisible by the length of the pattern.. the divisiblity number is equal to the number of occurrences

    if len(array_of_matches_indices) > 0 and len(array_of_matches_indices) % pattern_length == 0:
        return True
    else:
        return False



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    index_of_pattern = 0

    #the largest index
    pattern_index_length = len(pattern)

    #the length of the patterns
    pattern_length = len(pattern)

    #index of text
    index = 0

    #the number of overall matches
    matches = 0

    #the indices of the matches
    array_of_matches_indices = []

    #temporary array to hold the matching indices
    temp_array_of_matches = []

    #determines if pattern is an empty string if so
    #return True
    if pattern == '':
        return 0

    #loop condition that defines whether the index of the text has reached the length of the text
    while index < len(text):

        #condition to check if the pattern and the text share the same character at the designated index
        if pattern[index_of_pattern] == text[index]:
            temp_array_of_matches.append(index)

            index_of_pattern += 1
            index += 1
            matches += 1

            #determines if the number of matches equates to the number of characters in the pattern than we'll move the indices stored within the temp array to the permanent array
            if matches == pattern_length:
                array_of_matches_indices.extend(temp_array_of_matches)
                matches = 0
                index_of_pattern = 0

            #determines if the index exceed the actual length of the text
            if index == len(text):
                break

        #in the case of the characters not matching we revert the pattern back to the first character, reset the number of matches and clear the temp array
        if pattern[index_of_pattern] != text[index]:
            index_of_pattern = 0
            matches = 0
            temp_array_of_matches = []

            #if after the changes above we the two characters don't equate then we will go to the next character within the text to compare
            if pattern[index_of_pattern] != text[index]:
                index += 1


    if len(array_of_matches_indices) > 0:
        return array_of_matches_indices[0]
    else:
        return None



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
