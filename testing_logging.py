"""
This is exercise with testing and logging
"""
## STEPS TO COMPLETE ##
# 1. import logging
# 2. set up config file for logging called `test_results.log`
# 3. add try except with logging and assert tests for each function
#    - consider denominator not zero (divide_vals)
#    - consider that values must be floats (divide_vals)
#    - consider text must be string (num_words)
# 4. check to see that the log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score

import logging

logging.basicConfig(
    filename="./test_results.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s"
)

def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:

        fraction_val = numerator/denominator
        assert isinstance(numerator, float)
        assert isinstance(denominator, float)
        logging.info("SUCCESS - Results : %s", fraction_val)
        return fraction_val
    except ZeroDivisionError:
        logging.error("Failed - denominator is zero")
        return "denominator cannot be zero"
    except AssertionError:
        logging.error("Failed - input must be float")
        return "input must be float"


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        assert isinstance(text, str)
        num_of_words = len(text.split())
        logging.info("SUCCESS - number of words are %s", num_words)
        return num_of_words
    except AssertionError:
        logging.error("Failed - text argument must be a string")
        return "text argument must be a string"

if __name__ == "__main__":
    divide_vals(3.4, 0)
    divide_vals(4.5, 2.7)
    divide_vals(-3.8, 2.1)
    divide_vals(1, 2)
    num_words(5)
    num_words('This is the best string')
    num_words('one')
