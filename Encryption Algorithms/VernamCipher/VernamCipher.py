""" 
VernamCipher is a text encrypting algorithm

Condition: The key length must match the length of the message.
"""


# Encrypting function
def encrypt(text, key):
    global decrypt_imp
    
    key = list(key)
    decrypt_imp = [] # important for decrypting
    result = ""

    j = -1
    for i in text:
        if j < len(key) - 1:
            j += 1
        else:
            j = 0
        temp = (ord(i) - 65)+ (ord(key[j]) - 65)
        
        k = 0
        while temp > 25:
            temp -= 26
            k += 1
        decrypt_imp.append(k)
    
        result += chr(temp + 65)
    return result
    
# Decrypting function
def decrypt(text, key):
    global decrypt_imp
    key = list(key)

    result = ""

    j = -1
    for i in text:
        if j < len(key) - 1:
            j += 1
        else:
            j = 0   

        k = 0

        temp = (ord(i) - 65)- (ord(key[j]) - 65)
        while True:
            if decrypt_imp[k] != 0:
                temp += 26
                decrypt_imp[k] -= 1
            else:
                k += 1
                break

        
        result += chr(temp + 65)
    return result
    

if __name__ == "__main__":

    # Taking input the plaintext and the key
    plain_text = input("Enter the text: ")
    keyword = input("Enter the Key: ")

    # Performing the encryption 
    encrypted_text = encrypt(plain_text, keyword)
    decrypted_text = decrypt(encrypted_text,keyword)
    print(encrypted_text)
    print(decrypted_text)


"""
# Output
    Enter the text: HELLO
    Enter the Key: DGHBC
    KKSMQ
    HELLO
"""
