def encode(text, shift):
    result = ""
    for i in range(len(text)):
        if text[i].isupper():
            result += chr((ord(text[i]) + shift - 65) % 26 + 65)
        elif text[i].islower():
            result += chr((ord(text[i]) + shift - 97) % 26 + 97)
        else:
            result += text[i]
    return result

def decode(ciphertext, shift):
    result = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isupper():
            result += chr((ord(ciphertext[i]) - shift - 65 + 26) % 26 + 65)
        elif ciphertext[i].islower():
            result += chr((ord(ciphertext[i]) - shift - 97 + 26) % 26 + 97)
        else:
            result += ciphertext[i]
    return result

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encode Text")
        print("2. Decode Text")
        print("3. Exit")
        choice = input("Enter Your Choice: ")
        
        if choice == "1" or choice == "2":
            text = input("\nEnter The Text: ")
            shift = int(input("Enter The Shift Value: "))
            
            if choice == "1":
                print("\nEncoded Text:", encode(text, shift))
            else:
                print("\nDecoded Text:", decode(text, shift))
        elif choice == "3":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Choose Again!")

if __name__ == "__main__":
    main()
