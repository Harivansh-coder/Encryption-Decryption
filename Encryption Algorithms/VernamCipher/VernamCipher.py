""" 
VernamCipher is a text encrypting algorithm

Condition: The key length must match the length of the message.
"""


# Encrypting function
def encrypt(text, key):

    # checking if the condition meets
    if len(key) != len(text):
        return "Both key and text should be of same length"
    
    decrypt_imp = {}
    result = ""
    for i, j in zip(text,key):
        temp = (ord(i) - 65)+ (ord(j) - 65)
        
        k = 0
        while temp > 25:
            temp -= 26
            k += 1

        
        result += chr(temp + 65)
        decrypt_imp[result] = k
    return result
    


if __name__ == "__main__":

    # Taking input the plaintext and the key
    plain_text = input("Enter the text: ")
    keyword = input("Enter the Key: ")

    # Performing the encryption 
    encrypted_text = encrypt(plain_text, keyword)

    print(encrypted_text)


"""
#Output
    Enter the text: HELLO
    Enter the Key: DGHBC
    KKSMQ
"""