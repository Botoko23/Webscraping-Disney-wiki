import pytest
from money_conversion import money_converter
def test_standard():
	assert money_converter("$3 million") == 3_000_000

def test_standard_double_digit():
	assert money_converter("$99 million") == 99_000_000

def test_standard_with_decimal():
	assert money_converter("$3.5 million") == 3_500_000

def test_standard_multiple_decimals():
	assert money_converter("$1.234 million") == 1_234_000

def test_standard_billion():
	assert money_converter("$1.25 billion") == 1_250_000_000

def test_standard_thousand():
	assert money_converter("$900.9 thousand") == 900900

def test_range():
	assert money_converter("$3.6–4 million") == 3_600_000
	
def test_range_with_double_dollar():
	assert money_converter("$76.4–$83.3 million") == 76_400_000

def test_range_with_to():
	assert money_converter("$3.5 to 4 million") == 3_500_000

def test_number():
	assert money_converter("$950000") == 950000
	
def test_number_with_commas_space():
	assert money_converter("$5, million") == 5_000_000

def test_number_with_commas():
	assert money_converter("$127,850,000") == 127_850_000

def test_number_with_commas_and_decimals():
	assert money_converter("$10,000,000.50") == 10_000_000.5

def test_number_with_commas_middle():
	assert money_converter("estimated $5,000,000 (USD)") == 5_000_000

# def test_unkown():
# 	assert money_converter("70 crore") == ""

def test_empty():
	assert money_converter("") == ""