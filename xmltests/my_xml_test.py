import unittest

from my_xml import do_it

class MyXMLTests(unittest.TestCase):

    def test_find_mkey_leaf(self):
        self.assertEqual(
            1,
            do_it("c:\\Users\\adroissart\\exercism\\python\\xmltests\\input.xml")
        )

if __name__ == '__main__':
    unittest.main()