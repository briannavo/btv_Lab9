
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")

def encode_password(password):
    new_password = ''
    password = str(password)
    for num in password:
        num = int(num)
        num += 3
        new_password += str(num)

    return int(new_password)


while True:
    print_menu()
    option = input("Please enter an option: ")
    encoded_password = 0
    original_password = 0
    if option == "1":
        password_to_encode = int(input("Please enter your password to encode: "))
        original_password = password_to_encode
        encoded_password = encode_password(password_to_encode)
        print("Your password has been encoded and stored!")

        print(f"{encoded_password}")

    if option == '3':
        break

# Raul Rojas