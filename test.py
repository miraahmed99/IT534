import unittest
from main import VariableSort

class TestVariableSort(unittest.TestCase):
    def setUp(self): # initialize instance
        self.VariableSorter = VariableSort()

    def test_string(self): #tests valid string
        self.VariableSorter.add_variables("mir")
        self.assertEqual(self.VariableSorter.get_strings(), ["mir"])

    def test_integers(self): #tests valid integer
        self.VariableSorter.add_variables(5)
        self.assertEqual(self.VariableSorter.get_integers(), [5])

    def test_float(self): #tests valid float
        self.VariableSorter.add_variables(3.2)
        self.assertEqual(self.VariableSorter.get_floats(), [3.2])

    def test_invalid_string(self): #tests invalid integer
        with self.assertRaises(ValueError):
            self.VariableSorter.add_variables("mir123")

    def test_bad_type(self): #tests bad type
        with self.assertRaises(TypeError):
            self.VariableSorter.add_variables([1, 2, 3])


if __name__ == '__main__':
    unittest.main()