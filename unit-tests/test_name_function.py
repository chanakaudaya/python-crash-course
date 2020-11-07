import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Chanaka Udaya Kumara' work?"""
        formatted_name = get_formatted_name("chanaka","kumara","udaya")
        self.assertEqual(formatted_name, 'Chanaka Udaya Kumara')

if __name__ == '__main__':
    unittest.main()