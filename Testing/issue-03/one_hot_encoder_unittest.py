from one_hot_encoder import fit_transform
import unittest

class Test_one_hot_encoder(unittest.TestCase):
    #1
    def test_empty_element(self):
        actual = []
        self.assertRaises(TypeError, fit_transform(actual))
    #2
    def test_number_element(self):
        element = 123
        self.assertRaises(TypeError, fit_transform, element)
    #3
    def test_one_text_element(self):
        element = ['London']
        actual = fit_transform(*element)
        expected = [('London', [1])]
        self.assertEqual(actual, expected)
    #4
    def test_many_text_elements(self):
        element = ['Sos', 'Moscow', '12']
        actual = fit_transform(*element)
        expected = [('Sos', [0, 0, 1]), ('Moscow', [0, 1, 0]), ('12', [1, 0, 0])]
        self.assertEqual(actual, expected)
    #5
    def test_entry_elements(self):
        element = ['A', 'a']
        actual = fit_transform(*element)
        expected = [('A', [0, 1]), ('b', [ 1, 0])]
        self.assertNotEqual(actual, expected)
