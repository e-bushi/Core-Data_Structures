from set_adt import Set
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert len(s.groups) == 2
        assert s.total_num_of_group_elements == 0
        s = Set(4)
        assert len(s.groups) == 4
        assert s.total_num_of_group_elements == 0




    def test_add_group(self):
        s = Set()
        assert len(s.groups) == 2
        s.add_group({})
        assert len(s.groups) == 3
        s.add_group({})
        assert len(s.groups) == 4


    def test_add_element_to_group(self):
        s = Set()
        assert len(s.groups) == 2
        s.add_element_to_group(0, "Chris")
        assert s.groups[0]["Chris"] == True
        s.add_element_to_group(1, "Johnny")
        assert s.groups[1]["Johnny"] == True



    def test_remove(self):
        s = Set()
        assert len(s.groups) == 2
        s.remove_group(1)
        assert len(s.groups) == 1




    def test_contains(self):
        pass
