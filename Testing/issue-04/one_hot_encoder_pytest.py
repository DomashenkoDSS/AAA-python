from one_hot_encoder import fit_transform
import pytest


#1
def test_empty_element():
    actual = []
    with pytest.raises(TypeError):
        assert fit_transform(*actual)
#2
def test_number_element():
    element = 123
    with pytest.raises(TypeError):
        assert fit_transform(*element)
#3
def test_one_text_element():
    element = ['London']
    actual = fit_transform(*element)
    expected = [('London', [1])]
    assert actual==expected
#4
def test_many_text_elements():
    elements = ['Sos', 'Moscow', '12']
    actual = fit_transform(*elements)
    expected = [('Sos', [0, 0, 1]), ('Moscow', [0, 1, 0]), ('12', [1, 0, 0])]
    assert actual==expected

