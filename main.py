
def function():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


# def encode():

# def decode():

if __name__ == '__main__':
    norm_pass = None
    while True:
        function()
        option = input("Please enter an option: ")
        if option == "1":
            norm_pass = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
        if option == "2":
            code_pass = None
            for char in norm_pass:
                char = int(char) + 3
                if char >= 10:
                    char -= 10
                code_pass = str(code_pass) + str(char)
            print(f"The encoded password is {code_pass}, and the original password is {norm_pass}.")
        if option == "3":
            break