"""
Program to decrypt the encryped message.
"""
original_mess = ""

# decryption function
def decrypt(t,key):
    global original_mess

    j = 0
    for i in t:
        if j < 32:
            j += 1
        else:
            j = 1 

        temp = key[j - 1]

        character = ord(i) - temp

        if character == 32:
            original_mess += chr(character)
        else:
            character = chr(ord(i) + j)
            original_mess += character

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
    