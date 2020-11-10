import numpy

# Function to determine the size of the array
def set_arr_size():
    arr_size = None
    while arr_size == None:
        try:
            temp_arr_size = input("Please input the size of the array as a positive integer: ")
            arr_size = int(temp_arr_size)
            if arr_size <= 0:
                print("Array size must be a positive integer.")
                arr_size = None
            else:
                return arr_size
        except ValueError:
            print("'", temp_arr_size, "'", " is not an integer.", sep='')

# Function to gather elements for the array
# Input 'a' is the given size of the array
def set_arr_vals(a):
    my_array = []
    for i in range(a):
        check = 0
        while check == 0:
            try:
                err_arr_val = input("Please input an integer: ")
                arr_val = int(err_arr_val)
            except ValueError:
                print("'", err_arr_val, "'", " is not an integer.", sep='')
            else:
                my_array.append(int(arr_val))
                check = 1
    my_array = numpy.array(my_array)                # Convert list to array
    print("Here is the given array: ", my_array)
    return my_array

# Function to set the test value
def set_test_num():
    while True:
        try:
            test_num = input("Please input the integer to test against the array: ")
            return int(test_num)
        except ValueError:
            print("'", test_num, "'", " is not an integer.", sep='')

# Function to determine how many values are above and below the given value
# Input 'arr' is the array previously taken as input
# Input 'test_num' is the number being tested against the array
def get_abv_blw(arr, test_num):
    num_above = 0
    num_below = 0
    for j in arr:
        if test_num > j:
            num_below += 1
        elif test_num < j:
            num_above += 1
    return (num_above, num_below)

# Main
def main():
    a = set_arr_size()                                  # Get array size
    arr = set_arr_vals(a)                               # Set values in array
    testNum = set_test_num()                            # Set the test value
    (above, below) = get_abv_blw(arr, testNum)          # Get answer values
    print("above: ", above, ", below: ", below)         # Print answer

if __name__ == "__main__":
	main()
