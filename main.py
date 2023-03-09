def encode(password):
    pass

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode", "\n2. Decode", "\n3. Quit")

def main():
    while True:
        print_menu()
        print()
        option = input("Please enter an option: ")
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_p = encode(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            decoded_p = decode(password)
            print(f"The encoded password is {encoded_p}, and the original password is {decoded_p}.")
        if option == 3:
            break
        else:
            print("That is not a valid option. Try again")





if __name__ == "__main__":
    main()