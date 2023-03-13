# Math is truly fascinating. Since PI is much more frequently used than euler's number I decided to play with exactly this legendary constant.
##############################################


# Euler's number (without importing libraries)
e = 1 + 1/1 + 1/(1 * 2) + 1/(1 * 2 * 3) + 1/(1 * 2 * 3 * 4) + 1/(1 * 2 * 3 * 4 * 5) + 1/(1 * 2 * 3 * 4 * 5 * 6) + 1/(1 * 2 * 3 * 4 * 5 * 6 * 7) + 1/(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8) + 1/(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9) + 1/(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)
print(e)

# Euler's number to a string and removing the comma
e_str = str(e).replace('.', '')
print(e_str)

# Shifts the digits of the number one place to the left
e_shifted = e_str[1:] + e_str[0]
print(e_shifted)

# Removing all instances of "0" from the number
e_clean = ''.join([x for x in e_shifted if x != '0'])

# Result
print(e_clean)

##############################################
##############################################
#My next code should be : writing an algorithm that will search through the output (''e_shifted''), find the beginning of euler's number
#(let's say the first 4 digits), and finally sort the number back to the original order and add the comma.
