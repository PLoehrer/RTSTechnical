# RTSTechnical
This repository contains the solutions to the 3 problems contained in the untimed technical interview for RTS Labs. 

  The solution for problem #1 requires the "numpy" module to be installed. When run, problem1final.py will ask the user for the desired length of the array. 
Then it will ask the user to fill the array with integers. Finally, it will ask the user for an integer to test against the array and show how many values 
in the array are above and below the given test value.
  
  The set_arr_size() method uses a while loop to ask the user for a positive integer input until the input is successfully received. If the user inputs anything
other than a positive integer, the loop will cycle again and ask the user again for a positive integer. 
  
  The set_arr_vals() method uses a for loop to iterate through the positions in the array created in the set_arr_size() method and places integer values in each 
position. If the user inputs anything other than an integer value, the method will ask the user again to enter an integer.
  
  The set_test_num() method asks the user for an integer number to test against the array. If the user enters anything other than an integer the method will 
ask the user again to enter an integer.
  
  The get_abv_blw() method takes the array and test number as inputs and produces the quantity of values in the array above the test value and the number below 
the test value.



  The solution for problem #2 takes a string as an input and an integer as an input and rotates the string by the given integer. 
  
  The set_string() method takes a string of characters as input. If the user does not input a string of at least length 1, the method will ask again for the 
user to input a string.
  
  The get_rot_val() method asks the user to input an integer that will be used to rotate the string. If the user does not input an integer, the method
will ask again for an integer.
  
  The rot_string() method takes the string and the rotation value as inputs and rotates the string by the value given. If the given value is a positive 
integer, the characters will be moved from the back of the string to the front. If the given value is a negative integer, the characters will be moved
from the front of the string to the back. 
