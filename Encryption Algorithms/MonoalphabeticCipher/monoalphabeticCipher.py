"""
A old and simple encryption algorithm works on mono-alphabetic substitution method.
"""

def encrypt(text):
    result = ""
    for i in text:
        if i == 'm':
            i = 'a'
        elif i == 'a':
            i = 'z'
        result += i
    
    return result

def decrypt(text):
    result = ""
    for i in text:
        if i == 'a':
            i = 'm'
        elif i == 'z':
            i = 'a'
        result += i
    
    return result

if __name__ == "__main__":

    text = input("Enter the text: ")

    cipher_text = encrypt(text)

    print("The cipher text is: ",cipher_text)
    print("The original text: ",decrypt(cipher_text))

"""
# Output:

    Enter the text: Monoalphabetic cipher
    The cipher text is:  Monozlphzbetic cipher
    The original text:  Monoalphabetic cipher 
"""