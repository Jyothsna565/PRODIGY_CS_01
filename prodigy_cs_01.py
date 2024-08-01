#Caesar Cipher Encryption and Decryption

#This Python script implements the Caesar Cipher algorithm to encrypt and decrypt messages.
#The Caesar Cipher shifts each letter in the message by a fixed number of positions in the alphabet.

def caesar_cipher(text, shift, mode):
    alphabets = {
        "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "lowercase": "abcdefghijklmnopqrstuvwxyz"
    }
    result = ""

    for char in text:
        if char in alphabets["uppercase"] or char in alphabets["lowercase"]:
            if char.isupper():
                index = alphabets["uppercase"].index(char)
            else:
                index = alphabets["lowercase"].index(char)

            if mode == "encrypt":
                new_index = (index + shift) % 26
            elif mode == "decrypt":
                new_index = (index - shift) % 26

            if char.isupper():
                result += alphabets["uppercase"][new_index]
            else:
                result += alphabets["lowercase"][new_index]
        else:
            result += char

    return result

def main():
    while True:
        choice = input("Do you want to encrypt (E) or decrypt (D) a message? (E/D): ").strip().lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
            continue

        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (an integer): "))

        if choice == 'e':
            encrypted_message = caesar_cipher(message, shift, "encrypt")
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher(message, shift, "decrypt")
            print("Decrypted message:", decrypted_message)

        another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
