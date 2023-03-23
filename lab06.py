# Joanna Mijares
# Lab 06 Encoding/ Decoding

# Lab partner is Sallie Zhou

def menu(): # Prints out menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

# Encodes the password by checking if each character in the password string is a number. If it is indeed a number, then it will be converted to an integer,
# 3 will be added, and then placed back into a string.
def encode_pass(password):
    encoded_pass = ''
    for i in password:
        if i.isdigit():
            encoded_pass += str(int(i) + 3)
        else:
            pass
    return encoded_pass

# Decodes the password by checking if each character in the password string is a number. If it is indeed a number, then it will be converted to an integer,
# 3 will be subtracted, and then placed back into a string.
def decode_pass(encoded_pass):
    decoded_pass = ""
    for digit in encoded_pass:
        if digit.isdigit():
            decoded_pass += str(int(digit) - 3)
    return decoded_pass


if __name__ == "__main__":

    # While True will ensure that the main function loops until it breaks
    while True:

        menu()
        print("")

        menu_option = int(input("Please enter an option: "))

        # If 1 is inputted, then you will be asked to input a passcode which will then be encoded by my encode_pass function
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode_pass(password)
            print("Your password has been encoded and stored!")
            print("")
        
        # If 2 is inputted, the previously encoded function will be decoded and both the encoded and decoded passwords will be read back to you.
        if menu_option == 2:
            decoded_pass = decode_pass(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")
            print()
            
        # Quits the program
        elif menu_option == 3:
            break
