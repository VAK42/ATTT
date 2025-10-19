def generateKey(str, key):
    x = len(str)
    i = 0
    while True:
        if x == i:
            i = 0
        if len(key) == len(str):
            break
        key += key[i]
        i += 1
    return key

def encode(str, key):
    cipherText = ""
    for i in range(len(str)):
        if str[i].isalpha():
            x = (ord(str[i].upper()) + ord(key[i].upper())) % 26
            if str[i].isupper():
                cipherText += chr(x + ord('A'))
            else:
                cipherText += chr(x + ord('a'))
        else:
            cipherText += str[i]
    return cipherText

def decode(cipherText, key):
    origText = ""
    for i in range(len(cipherText)):
        if cipherText[i].isalpha():
            x = (ord(cipherText[i].upper()) - ord(key[i].upper()) + 26) % 26
            if cipherText[i].isupper():
                origText += chr(x + ord('A'))
            else:
                origText += chr(x + ord('a'))
        else:
            origText += cipherText[i]
    return origText

def main():
    while True:
        print("\nVigenère Cipher Program")
        print("1. Encode Text")
        print("2. Decode Text")
        print("3. Exit")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1 or choice == 2:
            text = input("\nEnter The Text: ")
            key = input("Enter The Key: ")
            
            if len(key) != len(text):
                print("Key Length Must Match The Text Length!")
                continue
            
            keyGenerated = generateKey(text, key)
            
            if choice == 1:
                print("\nEncoded Text:", encode(text, keyGenerated))
            else:
                print("\nDecoded Text:", decode(text, keyGenerated))
        elif choice == 3:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Choose Again!")

if __name__ == "__main__":
    main()
