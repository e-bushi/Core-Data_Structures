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

    matches = 0

    #the indices of the matches
    array_of_matches_indices = []

    temp_array_of_matches = []

    if pattern == '':
        return True

    while index < len(text):

        if pattern[index_of_pattern] == text[index]:
            temp_array_of_matches.append(index)

            index_of_pattern += 1
            index += 1
            matches += 1

            if matches == pattern_length:
                array_of_matches_indices.extend(temp_array_of_matches)
                matches = 0
                index_of_pattern = 0

                if index == len(text):
                    break

        if pattern[index_of_pattern] != text[index]:
            index_of_pattern = 0
            matches = 0
            temp_array_of_matches = []

            if pattern[index_of_pattern] != text[index]:
                index += 1


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
