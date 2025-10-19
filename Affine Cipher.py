a = 17
b = 20

def encode(msg):
    cipher = ""
    for i in range(len(msg)):
        if msg[i].isalpha():
            if msg[i].isupper():
                cipher += chr((((a * (ord(msg[i]) - ord('A'))) + b) % 26) + ord('A'))
            else:
                cipher += chr((((a * (ord(msg[i]) - ord('a'))) + b) % 26) + ord('a'))
        else:
            cipher += msg[i]
    return cipher

def decode(cipher):
    msg = ""
    aInv = 0
    flag = 0
    for i in range(26):
        flag = (a * i) % 26
        if flag == 1:
            aInv = i
    
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            if cipher[i].isupper():
                msg += chr(((aInv * ((ord(cipher[i]) - ord('A') - b + 26) % 26)) % 26) + ord('A'))
            else:
                msg += chr(((aInv * ((ord(cipher[i]) - ord('a') - b + 26) % 26)) % 26) + ord('a'))
        else:
            msg += cipher[i]
    return msg

def main():
    while True:
        print("\nAffine Cipher Program")
        print("1. Encode Text")
        print("2. Decode Text")
        print("3. Exit")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1 or choice == 2:
            text = input("\nEnter The Text: ")
            if choice == 1:
                print("\nEncoded Text:", encode(text))
            else:
                print("\nDecoded Text:", decode(text))
        elif choice == 3:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Choose Again!")

if __name__ == "__main__":
    main()
