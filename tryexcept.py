def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    # try to return the fraction but if the denominator is zero
    # catch the error and return a string saying: 
    # "denominator cannot be zero"
    try:
        fraction_val = numerator/denominator
        return fraction_val
    except ZeroDivisionError:
        print("denominator cannot be zero")

def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    # try to split based on spaces and return num of words
    # but if text isnt a string return "text argument must be a string"
    try:
        num_words = len(text.split())
        return num_words
    except AttributeError:
        print("text argument must be a string")

if __name__ == "__main__":
    print(divide_vals(10,1))
    print(num_words("I am a student"))