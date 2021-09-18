"""
RSA algorithm implemented
"""

def inverse_mod(a, m):    
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


def encrypt(c, d, n):
    """
    c = message
    d = inverse mod
    n = p * q    

    """

    return (c**d)%n

def decrypt(m,e,n):

    """
    m = encrrypted message
    
    n = p * q    

    """

    return (m**e)%n



if __name__ == "__main__":

    p = int(input("Enter p: "))
    q = int(input("Enter q: "))

    message = int(input("Enter the message: "))

    n = p*q

    phi = (p-1) * (q-1)

    e = int(input("Enter the e: "))

    d = inverse_mod(e,phi)
    encrypt_mess = encrypt(message, d,n)

    print("Encrypted message = ",encrypt_mess)
    print("Decrypted message = ",decrypt(encrypt_mess,e,n))

"""
# Output

    Enter p: 17
    Enter q: 11
    Enter the message: 2
    Enter the e: 7
    Encrypted message =  162
    Decrypted message =  2

"""
