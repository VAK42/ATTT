def rightRotate(value, shift):
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF

def sha256(message):
    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
    
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19
    
    messageBytes = bytearray(message.encode())
    originalLength = len(messageBytes) * 8
    
    messageBytes.append(0x80)
    
    while len(messageBytes) % 64 != 56:
        messageBytes.append(0x00)
    
    messageBytes += originalLength.to_bytes(8, byteorder='big')
    
    for offset in range(0, len(messageBytes), 64):
        chunk = messageBytes[offset:offset + 64]
        w = [int.from_bytes(chunk[i:i+4], byteorder='big') for i in range(0, 64, 4)]
        
        for i in range(16, 64):
            s0 = rightRotate(w[i-15], 7) ^ rightRotate(w[i-15], 18) ^ (w[i-15] >> 3)
            s1 = rightRotate(w[i-2], 17) ^ rightRotate(w[i-2], 19) ^ (w[i-2] >> 10)
            w.append((w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF)
        
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7
        
        for i in range(64):
            s1 = rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + s1 + ch + k[i] + w[i]) & 0xFFFFFFFF
            s0 = rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (s0 + maj) & 0xFFFFFFFF
            
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF
        
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF
    
    result = h0.to_bytes(4, byteorder='big') + h1.to_bytes(4, byteorder='big') + h2.to_bytes(4, byteorder='big') + h3.to_bytes(4, byteorder='big') + h4.to_bytes(4, byteorder='big') + h5.to_bytes(4, byteorder='big') + h6.to_bytes(4, byteorder='big') + h7.to_bytes(4, byteorder='big')
    return ''.join(f'{b:02x}' for b in result)

def compareSha256():
    string1 = input("\nEnter First String: ")
    string2 = input("Enter Second String: ")
    
    hash1 = sha256(string1)
    hash2 = sha256(string2)
    
    print("\nSHA256 Of First String:", hash1)
    print("SHA256 Of Second String:", hash2)
    
    if hash1 == hash2:
        print("\nResult: Two Strings Have The Same SHA256 Hash")
    else:
        print("\nResult: Two Strings Have Different SHA256 Hashes")

def passwordSystem():
    print("\n--- Registration ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    storedHash = sha256(password)
    print("Password Saved With SHA256 Hash:", storedHash)
    
    print("\n--- Login ---")
    loginUsername = input("Enter Username: ")
    loginPassword = input("Enter Password: ")
    loginHash = sha256(loginPassword)
    
    if loginUsername == username and loginHash == storedHash:
        print("\nLogin Successful!")
    else:
        print("\nLogin Failed! Invalid Credentials!")

def main():
    while True:
        print("\nSHA256 Hash Program")
        print("1. Compare SHA256 Hash Of Two Strings")
        print("2. Password System With SHA256")
        print("3. Exit")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            compareSha256()
        elif choice == 2:
            passwordSystem()
        elif choice == 3:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Choose Again!")

if __name__ == "__main__":
    main()
