''' 
Import statements: 
    1. Import pytest and spellcheck modules
    2. Using the "try-except: will throw error.
    3. Comment "raise NotImplementedError"
'''
### WRITE IMPORT STATEMENTS HERE
import pytest
import spellcheck

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string has fewer than 10 words
        2. Use an assert statement to check the given string has fewer than 50 chars

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE
    # try:
    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char_count(input_value) <50
    # except:
        # raise NotImplementedError()

# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string begins with a capital letter
        2. Use an assert statement to check the given string end with a period ('.')

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE
    # try:
    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value) == "."
    # except:
        # raise NotImplementedError()

# Run these tests with `python3 -m pytest test_spellcheck.py`