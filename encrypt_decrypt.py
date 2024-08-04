def caesar_cipher(message, shift, mode='encrypt'):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.

    Parameters:
    message (str): The input message to encrypt or decrypt.
    shift (int): The number of positions to shift each character.
    mode (str): Mode of operation - 'encrypt' or 'decrypt'.

    Returns:
    str: The resulting encrypted or decrypted message.
    """
    result = ''
    if mode == 'decrypt':
        shift = -shift

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


# User input
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Choose mode ('encrypt' or 'decrypt'): ").strip().lower()

# Encrypt or decrypt
if mode in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift, mode)
    print(f"The {mode}ed message is: {output}")
else:
    print("Invalid mode selected. Choose 'encrypt' or 'decrypt'.")
