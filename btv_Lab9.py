# Brianna Vo
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

    return new_password


# code from Raul Rojas
def decode_password(encoded_password):
    original_password = ''
    encoded_password = str(encoded_password)
    for num in encoded_password:
        num = int(num)
        num -= 3
        original_password += str(num)  # Ensure digits wrap around below 0

    return original_password

def main():
    print_menu()
    while True:
        option = input("Please enter an option: ")
        if option == "1":
            password_to_encode = int(input("Please enter your password to encode: "))
            original_password = password_to_encode
            encoded_password = encode_password(password_to_encode)
            print("Your password has been encoded and stored!")
        if option == "2":
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is: {encoded_password}, and the original password is {decoded_password}")
        if option == '3':
            break

main()