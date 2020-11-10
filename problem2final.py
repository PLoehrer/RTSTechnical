# Function to take a string as input
def set_string():
    string = None
    while string == None:
        try:
            string = input("Please input a string of characters: ")
            if len(string) <= 0:
                print("String must contain at least 1 character.")
                string = None
            else:
                return string
        except ValueError:
            print("'", string, "'", " is not a string of characters.", sep='')

# Function to determine how many characters to rotate the string
def get_rot_val():
    while True:
        try:
            rot_val = input("Please input the amount to rotate the string as an integer: ")
            return int(rot_val)
        except:
            print("'", rot_val, "'", " is not an integer.", sep='')

# Function to perform the rotation on the string
def rot_string(string, rot):
    rot %= len(string)                  # Force rotation value to fit bounds of string length
    if rot > 0:
        return string[len(string)-rot:] + string[:len(string)-rot]  # Rotate back to front for positive integers
    return string[:len(string)-rot] + string[len(string)-rot:]      # Rotate front to back for negative integers

# Main
def main():
    string = set_string()
    val = get_rot_val()
    end_string = rot_string(string, val)
    print((string), "rotated by %d is" % (val), end_string)

if __name__ == "__main__":
	main()
