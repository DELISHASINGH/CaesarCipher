
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)

print("Caesar Cipher Encryption & Decryption")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
print("\nEncrypted Message:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted Message:", decrypted)

// completed of task 1

