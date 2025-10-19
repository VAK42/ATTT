import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extendedGCD(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extendedGCD(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modInverse(e, phi):
    gcd, x, y = extendedGCD(e, phi)
    if gcd != 1:
        return None
    return (x % phi + phi) % phi


def isPrime(n, k=5):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def generatePrime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1
        if isPrime(num):
            return num


def generateKeyPair(keySize):
    p = generatePrime(keySize // 2)
    q = generatePrime(keySize // 2)
    
    while p == q:
        q = generatePrime(keySize // 2)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = modInverse(e, phi)
    
    return ((e, n), (d, n), p, q)


def encrypt(plaintext, publicKey):
    e, n = publicKey
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(ciphertext, privateKey):
    d, n = privateKey
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext


def encryptNumber(number, publicKey):
    e, n = publicKey
    return pow(number, e, n)


def decryptNumber(cipherNumber, privateKey):
    d, n = privateKey
    return pow(cipherNumber, d, n)


def textToNumber(text):
    return int.from_bytes(text.encode(), 'big')


def numberToText(number):
    numBytes = (number.bit_length() + 7) // 8
    return number.to_bytes(numBytes, 'big').decode()


def main():
    publicKey = None
    privateKey = None
    p = None
    q = None
    
    while True:
        print("\nRSA Encryption Program")
        print("1. Generate RSA Keys")
        print("2. Encrypt Text")
        print("3. Decrypt Text")
        print("4. Encrypt Number")
        print("5. Decrypt Number")
        print("6. Display Keys")
        print("7. Exit")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            print("\nKey Size Options:")
            print("1. 512 Bits")
            print("2. 1024 Bits")
            print("3. 2048 Bits")
            print("4. Custom")
            keySizeChoice = int(input("Enter Your Choice: "))
            
            if keySizeChoice == 1:
                keySize = 512
            elif keySizeChoice == 2:
                keySize = 1024
            elif keySizeChoice == 3:
                keySize = 2048
            elif keySizeChoice == 4:
                keySize = int(input("Enter Key Size (Bits): "))
            else:
                print("Invalid Choice!")
                continue
            
            print(f"\nGenerating {keySize}-Bit RSA Keys...")
            publicKey, privateKey, p, q = generateKeyPair(keySize)
            print("Keys Generated Successfully!")
            print(f"Public Key (e, n): ({publicKey[0]}, {publicKey[1]})")
            print(f"Private Key (d, n): ({privateKey[0]}, {privateKey[1]})")
            
        elif choice == 2:
            if publicKey is None:
                print("\nPlease Generate Keys First!")
                continue
            
            plaintext = input("\nEnter Plaintext: ")
            ciphertext = encrypt(plaintext, publicKey)
            print(f"\nEncrypted Text: {ciphertext}")
            
        elif choice == 3:
            if privateKey is None:
                print("\nPlease Generate Keys First!")
                continue
            
            ciphertextInput = input("\nEnter Ciphertext (Space-Separated Numbers): ")
            ciphertext = [int(x) for x in ciphertextInput.split()]
            plaintext = decrypt(ciphertext, privateKey)
            print(f"\nDecrypted Text: {plaintext}")
            
        elif choice == 4:
            if publicKey is None:
                print("\nPlease Generate Keys First!")
                continue
            
            number = int(input("\nEnter Number To Encrypt: "))
            encrypted = encryptNumber(number, publicKey)
            print(f"\nEncrypted Number: {encrypted}")
            
        elif choice == 5:
            if privateKey is None:
                print("\nPlease Generate Keys First!")
                continue
            
            cipherNumber = int(input("\nEnter Encrypted Number: "))
            decrypted = decryptNumber(cipherNumber, privateKey)
            print(f"\nDecrypted Number: {decrypted}")
            
        elif choice == 6:
            if publicKey is None:
                print("\nNo Keys Generated Yet!")
                continue
            
            print(f"\nPublic Key:")
            print(f"  e (Exponent): {publicKey[0]}")
            print(f"  n (Modulus): {publicKey[1]}")
            print(f"\nPrivate Key:")
            print(f"  d (Exponent): {privateKey[0]}")
            print(f"  n (Modulus): {privateKey[1]}")
            print(f"\nPrime Factors:")
            print(f"  p: {p}")
            print(f"  q: {q}")
            print(f"  φ(n): {(p-1)*(q-1)}")
            
        elif choice == 7:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Choose Again!")


if __name__ == "__main__":
    main()
