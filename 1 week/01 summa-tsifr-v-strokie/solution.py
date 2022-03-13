import sys


def summ_digits():

    result = 0    
    digit_string = sys.argv[1]

    for digit in digit_string:
        result += int(digit)

    return result


if __name__ == '__main__':

    print(summ_digits())

