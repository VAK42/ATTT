def modInverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def determinant(keyMatrix):
    det = keyMatrix[0][0] * (keyMatrix[1][1] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][1])
    det -= keyMatrix[0][1] * (keyMatrix[1][0] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][0])
    det += keyMatrix[0][2] * (keyMatrix[1][0] * keyMatrix[2][1] - keyMatrix[1][1] * keyMatrix[2][0])
    return det % 26

def adjugate(keyMatrix, adj):
    adj[0][0] = keyMatrix[1][1] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][1]
    adj[0][1] = -(keyMatrix[0][1] * keyMatrix[2][2] - keyMatrix[0][2] * keyMatrix[2][1])
    adj[0][2] = keyMatrix[0][1] * keyMatrix[1][2] - keyMatrix[0][2] * keyMatrix[1][1]
    adj[1][0] = -(keyMatrix[1][0] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][0])
    adj[1][1] = keyMatrix[0][0] * keyMatrix[2][2] - keyMatrix[0][2] * keyMatrix[2][0]
    adj[1][2] = -(keyMatrix[0][0] * keyMatrix[1][2] - keyMatrix[0][2] * keyMatrix[1][0])
    adj[2][0] = keyMatrix[1][0] * keyMatrix[2][1] - keyMatrix[1][1] * keyMatrix[2][0]
    adj[2][1] = -(keyMatrix[0][0] * keyMatrix[2][1] - keyMatrix[0][1] * keyMatrix[2][0])
    adj[2][2] = keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0]

def inverse(keyMatrix, inverseMatrix):
    det = determinant(keyMatrix)
    det = (det + 26) % 26
    detInverse = modInverse(det, 26)
    if detInverse == -1:
        print("Inverse Doesn't Exist For The Given Matrix (Determinant Is 0 Modulo 26)!")
        return False
    
    adj = [[0 for _ in range(3)] for _ in range(3)]
    adjugate(keyMatrix, adj)
    
    for i in range(3):
        for j in range(3):
            inverseMatrix[i][j] = (adj[i][j] * detInverse) % 26
            if inverseMatrix[i][j] < 0:
                inverseMatrix[i][j] += 26
    return True

def getKeyMatrix(key, keyMatrix):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = (ord(key[k]) - ord('A')) % 26
            k += 1

def encrypt(cipherMatrix, keyMatrix, messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j]
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def decrypt(cipherMatrix, inverseMatrix, messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += inverseMatrix[i][x] * messageVector[x][j]
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def hillCipher(message, key, encrypting=True):
    keyMatrix = [[0 for _ in range(3)] for _ in range(3)]
    getKeyMatrix(key, keyMatrix)
    
    messageVector = [[0] for _ in range(3)]
    for i in range(3):
        messageVector[i][0] = ord(message[i]) - ord('A')
    
    cipherMatrix = [[0] for _ in range(3)]
    if encrypting:
        encrypt(cipherMatrix, keyMatrix, messageVector)
    else:
        inverseMatrix = [[0 for _ in range(3)] for _ in range(3)]
        if not inverse(keyMatrix, inverseMatrix):
            return
        decrypt(cipherMatrix, inverseMatrix, messageVector)
    
    resultText = ""
    for i in range(3):
        resultText += chr(cipherMatrix[i][0] + ord('A'))
    
    print("Ciphertext: " if encrypting else "Plaintext: ", resultText)

def main():
    while True:
        print("\nHill Cipher Program")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            message = input("Enter The Message (3 Characters): ")
            key = input("Enter The Key (9 Characters): ")
            if len(message) != 3 or len(key) != 9:
                print("Message Must Be 3 Characters & Key Must Be 9 Characters Long!")
            else:
                hillCipher(message, key, True)
        elif choice == 2:
            message = input("Enter The Message (3 Characters): ")
            key = input("Enter The Key (9 Characters): ")
            if len(message) != 3 or len(key) != 9:
                print("Message Must Be 3 Characters & Key Must Be 9 Characters Long!")
            else:
                hillCipher(message, key, False)
        elif choice == 3:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Choose Again!")

if __name__ == "__main__":
    main()
