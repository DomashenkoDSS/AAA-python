from unittest.mock import patch
import what_is_year_now as wyn
import pytest

def test_dot_date():
    with patch('what_is_year_now.json.load', return_value={'currentDateTime': '02.12.2020'}):
        assert wyn.what_is_year_now() == 2020

def test_dash_date():
    with patch('what_is_year_now.json.load', return_value={'currentDateTime': '2020-12-02'}):
        assert wyn.what_is_year_now() == 2020

def test_invalid_format_date():
    with patch('what_is_year_now.json.load', return_value={'currentDateTime': '02/12/2020'}):
        with pytest.raises(ValueError):
            wyn.what_is_year_now()

def test_format_initional():
    with patch('what_is_year_now.json.load', return_value={'currentDateTime': '0'}):
        with pytest.raises(IndexError):
            wyn.what_is_year_now()