"""
Program to encrypt the message.
"""
import random

# String for key and encrypted message
key = ""
encrypted_mess = ""

# method for encryption
def encrypt(t):
    global key
    global encrypted_mess

    for i in t:
        temp = random.randint(10,20)
        if i != ' ':
            key += str(temp)
            encrypted_mess += chr(ord(i) - temp)
        else:
            key += str(temp)
            encrypted_mess += chr(ord(i) + temp)


    return encrypted_mess

if __name__ == "__main__":

    # for reading message
    file = open("message.txt","rt")

    mess = file.read()

    # Call for encryption of message
    print(encrypt(mess))

    # key file created
    key_file = open("key.txt","a")
    key_file.write(key)

    file.close()
    key_file.close()
    
"""
# Output

    cV2PgR-Ma^ZfZ]bc3dR/NeW4^TVW\b0SiaQQa-ji▲
"""
