'''
This module is just a excercise in udacity nanodegree course
'''
## STEPS TO COMPLETE ##
# 1. import logging
# 2. set up config file for logging called `results.log`
# 3. add try except with logging for success or error
#    in relation to checking the types of a and b
# 4. check to see that log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score

import logging

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)


def sum_vals(first_variable, second_variable):
    '''
    Args:
        a: (int)
        b: (int)
    Return:
        a + b (int)
    '''
    try:
        check_val = first_variable + 1
        result = first_variable + second_variable
        print(f"SUCESS - Type of check_val is {check_val}")
        logging.info("SUCCESS - Result of function is ")
        return result
    except TypeError:
        logging.error("Fail - Invalid type with variable a or b")
        return None


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(4, 5)
