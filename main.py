
def function():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


# def encode():

# def decode():
# Wilson, Damian - edits start here (filling in decode)
def decode(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result

if __name__ == '__main__':
    norm_pass = None
    while True:
        function()
        option = input("Please enter an option: ")
        if option == "1":
            norm_pass = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
        if option == "2":

        if option == "3":
            break
