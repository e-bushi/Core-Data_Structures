from hashtable import HashTable

class Set(object):

    def __init__(self, number_of_groups=2):
        '''Initialize this set implementation with a Hash Table'''
        self.groups = {}

        self.total_num_of_group_elements = 0

        for i in range(number_of_groups):
            self.groups[i] = {}

    def __repr__(self):
        '''Return a string representation of set'''
        return "Set: {!r}".format(self.groups)

    def add_group(self, group):
        '''Add a group within a particular set'''
        #number of groups within the set
        set_length = len(self.groups)

        #adds a new group to the set
        self.groups[set_length] = group

    def add_element_to_group(self, key, element, b=True):
        '''Add element to a specific group within the set'''
        group = self.groups[key]
        group[element] = b


    def remove(self):
        '''Remove a group within the set'''
        pass


    def contains(self):
        '''Returns tuple with that has a boolean value
        and key of the group that contains element sought after, if element
        doesn't exist within the set than returns False'''
        pass



if __name__ == '__main__':
    s = Set(4)
    s.add_element_to_group(0, "Chris")
    s.add_element_to_group(1, "Johnny")
    print(s.__repr__())
