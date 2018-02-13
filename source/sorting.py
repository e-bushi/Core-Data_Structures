#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not
    #loop through elements within items
    for i in range(0, len(items) - 1):
        #check if element adjacent to element at index i is greater than itself, if not
        #return false because list is out of order
        if items[i] > items[i + 1]:
            return False
    #return true if for loop exits with out returning false
    return True


def swap(first, second, items):
    first_number = items[first]
    second_number = items[second]
    value_holder = 0

    value_holder = first_number
    first_number = second_number
    second_number = value_holder

    items[first] = first_number
    items[second] = second_number
    return items


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    #if items list is empty than return it without changes
    if len(items) == 0:
        return items

    #while loop will only exit when it is sorted
    while is_sorted(items) is False:
        #loop through indices of items
        for i in range(0, len(items) - 1):
            #if element at index i is greater that is adjacent element enter if statement
            if i == len(items) - 1:
                break

            if items[i] > items[i + 1]:
                #return a list with updated swapped values
                items = swap(i, i+1, items)

    #return sorted list
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    if len(items) == 0:
        return items

    unsorted_index = 0
    minimum = items[0]
    minimum_position = 0


    while is_sorted(items) is False:

        for i in range(unsorted_index, len(items) - 1):

            if items[i] < minimum:
                minimum = items[i]
                minimum_position = i

        items = swap(unsorted_index, minimum_position, items)

        if unsorted_index < len(items) - 1:
            unsorted_index += 1
            minimum = items[unsorted_index]
        else:
            unsorted_index = 0





def recursive_backwards_checker(left_indx, right_indx, items):
    """decrement backwards in the array to check against values"""
    while left_indx >= 0:

        if left_indx == right_indx:
            return items

        if items[right_indx] >= items[left_indx]:

            right_value = items.pop(right_indx)
            items.insert(left_indx+1, right_value)
            return (items, left_indx + 1)

        elif items[right_indx] < items[left_indx]:

            if left_indx == 0:
                right_value = items.pop(right_indx)
                items.insert(left_indx, right_value)
                return (items, left_indx + 1)
            else:
                left_indx -= 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    if len(items) == 0:
        return items

    while is_sorted(items) is False:
            left = 0
            right = 0

            while right <= len(items) - 1:

                items = recursive_backwards_checker(left, right, items)

                if isinstance(items, tuple):
                    items = items[0]
                    left = items[1]

                    if right - left != 1:
                        left = right

                right += 1

    return items





def merge(first_partition, second_partition, original_items):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    combined_sorted_array = []

    index_of_first_partition = 0
    index_of_second_partition = 0

    for i in range(0, len(original_items) - 1):

        if len(first_partition) == 0:
            combined_sorted_array.append(second_partition[index_of_second_partition])
            continue
        elif len(second_partition) == 0:
            combined_sorted_array.append(first_partition[index_of_first_partition])
            continue

        if first_partition[index_of_first_partition] < second_partition[index_of_second_partition]:
            value_popped = first_partition.pop(index_of_first_partition)

            combined_sorted_array.append(value_popped)
            print(combined_sorted_array)


        elif first_partition[index_of_first_partition] == second_partition[index_of_second_partition]:
            first_value_popped = first_partition.pop(index_of_first_partition)
            second_value_popped = second_partition.pop(index_of_second_partition)

            combined_sorted_array.append(first_value_popped)
            combined_sorted_array.append(second_value_popped)
            print(combined_sorted_array)

        else:
            value_popped = second_partition.pop(index_of_second_partition)
            combined_sorted_array.append(value_popped)
            print(combined_sorted_array)


    print("This one is sorted -----> {}".format(combined_sorted_array))
    return combined_sorted_array


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    index_to_split_on = int(len(items) / 2)
    length_of_items = len(items)

    first_partition = items[:index_to_split_on]
    second_partition = items[index_to_split_on:]

    # TODO: Sort each half using any other sorting algorithm
    selection_sort(first_partition)
    selection_sort(second_partition)

    # TODO: Merge sorted halves into one list in sorted order
    items[:] = merge(first_partition, second_partition, items)




def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) < 2:
        return items

    index_to_split_on = len(items) // 2

    first_partition = items[:index_to_split_on]
    second_partition = items[index_to_split_on:]

    merge_sort(first_partition)
    merge_sort(second_partition)


    items[:] = merge(first_partition, second_partition, items)



def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=split_sort_merge, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
