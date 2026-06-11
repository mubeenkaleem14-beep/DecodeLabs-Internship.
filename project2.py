def encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)

if __name__ == "__main__":
    message = input("Enter text to encrypt: ")
    key = int(input("Enter shift key (e.g., 3): "))

    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print("\nOriginal Message →", message)
    print("Encrypted Message →", encrypted)
    print("Decrypted Message →", decrypted)

