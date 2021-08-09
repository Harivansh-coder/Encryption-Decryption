"""
Rail Fence Cipher is an transposition cipher.
"""


def encrypt(text, depth):
    cipher_text = ""
    result = []
    temp = []
    j = 1

    for i in text:
        temp.append(i)
        if j == depth:
            result.append(temp)
            temp = []
            j = 0
        j += 1

   
    for i in range(depth):
        for j in range(len(result)):
            cipher_text += result[j][i]

    return cipher_text

            

def decrypt(text, depth):
    plain_text = ""

    result = []
    temp = []
    j = 1

    for i in text:
        temp.append(i)
        if j == (len(text) / depth):
            result.append(temp)
            temp = []
            j = 0
        j += 1

    

    for i in range(len(result)-1):
        for j in range(depth):
            plain_text += result[j][i]
    
    return plain_text
    
    

if __name__ == "__main__":

    # Taking input the text and depth    
    text = input("Enter the text: ")
    depth = int(input("Enter the depth: "))

    cipher_text = encrypt(text, depth)
    print(cipher_text)


    print(decrypt(cipher_text,depth))

"""
# Output

    Enter the text: abcdef
    Enter the depth: 3
    adbecf
    abcdef
"""