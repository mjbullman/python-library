
def caesar_cipher(string: str, key: int) -> str:
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_string = ""

    for char in string:
        isUpper = char.isupper()

        if isUpper:
            if char in alphabet_upper:
                index = alphabet_upper.index(char)
                new_index = (index + key) % 26
                encrypted_string += alphabet_upper[new_index]
            else:
                encrypted_string += char
        else:
            if char in alphabet_lower:
                index = alphabet_lower.index(char)
                new_index = (index + key) % 26
                encrypted_string += alphabet_lower[new_index]
            else:
                encrypted_string += char

    return encrypted_string
