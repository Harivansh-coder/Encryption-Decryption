"""
It is one of the oldest encryption technique.
Implemenmted by substitution of characters by shifting it with a number of characters s. 
"""

# funtion to encrypt the message
def encrypt(text,shift):

    encrypted_mess = ""

    for i in text:

        # for capital alphabets
        if (i.isupper()):
            temp = (ord(i)+ shift - 65)%26 + 65
            encrypted_mess += chr(temp)
        # for small alphabets
        else:
            temp = (ord(i)+ shift - 97)%26 + 97
            encrypted_mess += chr(temp)

    return encrypted_mess


# funtion to decrypt the cipher
def decrypt(text,shift):
    decrypted_mess = ""

    for i in text:

        # for capital alphabets
        if (i.isupper()):
            temp = (ord(i)- shift - 65)%26 + 65
            decrypted_mess += chr(temp)
        # for small alphabets
        else:
            temp = (ord(i)- shift - 97)%26 + 97
            decrypted_mess += chr(temp)

    return decrypted_mess


    
if __name__ == "__main__":

    # Reading the text message from the file
    mess_file = open("message.txt")
    text = mess_file.read()

    # taking input the shift value
    shift = int(input("Enter the number of character to shift: "))
    result = encrypt(text,shift)

    print("Cipher Text: ",result)

    print("Original Text",decrypt(result,shift))



