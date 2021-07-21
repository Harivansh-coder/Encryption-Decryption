"""
Program to encrypt the message
"""
import random

# String for key and encrypted message
key = ""
encrypted_mess = ""

# Funtion for key creation
def create_Key():
    global key

    key_arr = []
    for i in range(32):
        temp = random.randint(10,20)
        key_arr.append(temp)
        key += str(temp)
    return key_arr

# method for encryption
def encrypt(t):
    global encrypted_mess

    key_arr = create_Key()
    j = 0
    for i in t:
        if j < 32:
            j += 1
        else:
            j = 1

        temp = key_arr[j-1]
        

        if i != ' ':
            encrypted_mess += chr(ord(i) - temp)
        else:
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

    TU^Za*_-Wa,_gd0cdXV,^ZOh[d   
"""
