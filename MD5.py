def leftRotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
         5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
    
    k = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
         0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
         0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
         0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
         0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
         0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
         0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
         0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
         0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
         0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
         0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
         0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
         0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
         0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
         0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
         0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]
    
    messageBytes = bytearray(message.encode())
    originalLength = len(messageBytes) * 8
    
    messageBytes.append(0x80)
    
    while len(messageBytes) % 64 != 56:
        messageBytes.append(0x00)
    
    messageBytes += originalLength.to_bytes(8, byteorder='little')
    
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476
    
    for offset in range(0, len(messageBytes), 64):
        chunk = messageBytes[offset:offset + 64]
        m = [int.from_bytes(chunk[i:i+4], byteorder='little') for i in range(0, 64, 4)]
        
        a = a0
        b = b0
        c = c0
        d = d0
        
        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | ((~b) & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * i) % 16
            
            f = (f + a + k[i] + m[g]) & 0xFFFFFFFF
            a = d
            d = c
            c = b
            b = (b + leftRotate(f, s[i])) & 0xFFFFFFFF
        
        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF
    
    result = a0.to_bytes(4, byteorder='little') + b0.to_bytes(4, byteorder='little') + c0.to_bytes(4, byteorder='little') + d0.to_bytes(4, byteorder='little')
    return ''.join(f'{b:02x}' for b in result)

def compareMd5():
    string1 = input("\nEnter First String: ")
    string2 = input("Enter Second String: ")
    
    hash1 = md5(string1)
    hash2 = md5(string2)
    
    print("\nMD5 Of First String:", hash1)
    print("MD5 Of Second String:", hash2)
    
    if hash1 == hash2:
        print("\nResult: Two Strings Have The Same MD5 Hash")
    else:
        print("\nResult: Two Strings Have Different MD5 Hashes")

def passwordSystem():
    print("\n--- Registration ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    storedHash = md5(password)
    print("Password Saved With MD5 Hash:", storedHash)
    
    print("\n--- Login ---")
    loginUsername = input("Enter Username: ")
    loginPassword = input("Enter Password: ")
    loginHash = md5(loginPassword)
    
    if loginUsername == username and loginHash == storedHash:
        print("\nLogin Successful!")
    else:
        print("\nLogin Failed! Invalid Credentials!")

def main():
    while True:
        print("\nMD5 Hash Program")
        print("1. Compare MD5 Hash Of Two Strings")
        print("2. Password System With MD5")
        print("3. Exit")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            compareMd5()
        elif choice == 2:
            passwordSystem()
        elif choice == 3:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Choose Again!")

if __name__ == "__main__":
    main()
