def encode(password):
    encoded_p = ""
    for num in str(password):
        num = int(num) + 3
        encoded_p = encoded_p + str(num)
    return encoded_p


def decode(p):
    decoded_p = ""
    for num in str(p):
        num = int(num) - 3
        decoded_p = decoded_p + str(num)
    return decoded_p

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode", "\n2. Decode", "\n3. Quit")

def main():
    while True:
        print_menu()
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_p = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_p = decode(encoded_p)
            print(f"The encoded password is {encoded_p}, and the original password is {decoded_p}.")
        elif option == 3:
            break
        else:
            print("That is not a valid option. Try again")
        print()





if __name__ == "__main__":
    main()