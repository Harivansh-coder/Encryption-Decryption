"""
Rail Fence Cipher is an transposition cipher.
"""

# function to encrypt the message
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

            
# function to decrypt
def decrypt(text, depth):
    plain_text = ""
    
    length = (len(text) // depth)

    result = [[] for i in range(length)]

    z = 0

    for i in range(depth):
        for j in result:
            j.append(text[z])
            z += 1

    for i in range(len(result)):
        for j in range(depth):
            plain_text += result[i][j]
    
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

    Enter the text: Space time 
    Enter the depth: 2
    Saetmpc ie
    Space time

    Enter the text: attack on titans
    Enter the depth: 3
    aa  ttcotatknin
    attack on titan
"""