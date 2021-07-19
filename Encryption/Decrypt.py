"""
Program to decrypt the encryped message.
"""
original_mess = ""

# decryption function
def decrypt(t,key):
    global original_mess

    for i,j in zip(t,key):
        temp = ord(i) - j
        if temp == 32:
            original_mess += chr(temp)
        else:
            temp = chr(ord(i) + j)
            original_mess += temp

    return original_mess
    
    
if __name__ == "__main__":

    # Taking the encrypted text as input
    encrypted_mess = input("Enter the string: ")

    key_file = open("key.txt")

    key_t = key_file.read()
    key_i = []

    # making the array of key
    for i in range(len(key_t)):
        if i % 2 != 0:
            key_i.append(int(key_t[i-1:i+1]))

    print(decrypt(encrypted_mess,key_i))
