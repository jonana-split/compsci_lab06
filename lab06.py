# Joanna Mijares
# Lab 06 Encoding/ Decoding

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode_pass(password):
    encoded_pass = ''
    for i in password:
        if i.isdigit():
            encoded_pass += str(int(i) + 3)
        else:
            pass
    return encoded_pass


def decode_pass(encoded_pass):
    decoded_pass = ""
    for digit in encoded_pass:
        if digit.isdigit():
            decoded_pass += str(int(digit) - 3)
    return decoded_pass


if __name__ == "__main__":

    while True:

        menu()
        print("")

        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode_pass(password)
            print("Your password has been encoded and stored!")
            print("")
        if menu_option == 2:
            decoded_pass = decode_pass(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")
            print()
        elif menu_option == 3:
            break
