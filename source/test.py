



def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if item == array[index]:
        return index
    else:
        print(array[index])
        if index == len(array) - 1 and item != array[index]:
            return None

        index += 1
        return linear_search_recursive(array, item, index)



names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
print(linear_search_recursive(names, 'Kojin', index=0))
