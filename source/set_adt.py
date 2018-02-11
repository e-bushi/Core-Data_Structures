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

        if type(group) == dict:
            self.groups[set_length] = group
        elif type(group) == list:

            for item in group:
                 self.add_element_to_group(set_length, item)


    def add_element_to_group(self, key, element, b=True):
        '''Add element to a specific group within the set'''
        group = self.groups[key]
        group[element] = b

        self.total_num_of_group_elements += 1


    def number_of_elements(self):
        '''Return the number of total items there are in each set combined'''
        group = self.groups
        item_count = 0

        for item in group.values():

            for keys in item:

                item_count += 1

        self.total_num_of_group_elements = item_count

        return self.total_num_of_group_elements

    def remove_group(self, group):
        '''Remove a group within the set'''
        pass
        if group not in self.group.keys():
            raise KeyError("Key is not in set")

        del self.group[group]


    def remove_element_from_group(self, group, key):
        '''remove a specific element within a group in the set'''
        groups = self.groups

        del groups[group][key]



    def contains(self, element):
        '''Returns bool if element exists within the set'''
        groups = self.groups

        for group in groups.values():

            for item in group.keys():

                if element == item:
                    return True

        return False


    def union(self, other_group):
        '''Return a new set that is the union of this set and other_set'''
        groups = self.groups
        union_group = []
        union_set = Set()

        for group in groups.values():

            for item in group.keys():

                union_group.append(item)

        union_group.extend(other_group)
        union_set.add_group(union_group)

        return union_group





if __name__ == '__main__':
    s = Set(4)
    s.add_element_to_group(0, "Chris")
    s.add_element_to_group(1, "Johnny")
    group = ["Jon", "Nana", "Mumu"]
    s.union(group)
    print(s.__repr__())
