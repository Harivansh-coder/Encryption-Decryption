"""VigenereCipher is a text encrypting algorithm, 
it uses polyalphabetic substitution method to encrypt the text.
"""

# Encrypting function
def encrypt(text, key):
    key = list(key)
    result = ""

    j = -1
    for i in text:
        if j < len(key)-1:
            j += 1
        else:
            j = 0
        key_char = key[j]
        result += chr((ord(i) + ord(key_char)) % 26 + 65)

    return result


# Decrypting function
def decrypt(text, key):
    key = list(key)
    orginal_mess = ""

    j = -1
    for i in text:
        if j < len(key)-1:
            j += 1
        else:
            j = 0
        key_char = key[j]
        orginal_mess += chr((ord(i) - ord(key_char) + 26) % 26 + 65)

    return orginal_mess
    

if __name__ == "__main__":
    
    # Taking input the plaintext and the key
    plain_text = input("Enter the text: ")
    keyword = input("Enter the Key: ")

    # Performing the encryption and decryption
    encrypted_text = encrypt(plain_text, keyword)

    print(encrypted_text)
    print(decrypt(encrypted_text, keyword))

"""
#Output
    Enter the text: HEROHERALAL
    Enter the Key: OGGY
    VKXMVKXYZGR
    HEROHERALAL
"""
