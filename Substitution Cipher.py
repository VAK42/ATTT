def encode(plainTxt, key):
    cipherTxt = ""
    lowerLetrs = "abcdefghijklmnopqrstuvwxyz"
    upperLetrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict1 = {}
    
    for i in range(len(lowerLetrs)):
        dict1[lowerLetrs[i]] = key[i]
        dict1[upperLetrs[i]] = key[i].upper()
    
    for c in plainTxt:
        if c in dict1:
            cipherTxt += dict1[c]
        else:
            cipherTxt += c
    
    return cipherTxt

def decode(cipherTxt, key):
    decryptTxt = ""
    lowerLetrs = "abcdefghijklmnopqrstuvwxyz"
    upperLetrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict2 = {}
    
    for i in range(len(lowerLetrs)):
        dict2[key[i]] = lowerLetrs[i]
        dict2[key[i].upper()] = upperLetrs[i]
    
    for c in cipherTxt:
        if c in dict2:
            decryptTxt += dict2[c]
        else:
            decryptTxt += c
    
    return decryptTxt

def isValidKey(key):
    # Check if key is 26 characters
    if len(key) != 26:
        return False
    
    # Check if key contains only alphabetic characters
    if not key.isalpha():
        return False
    
    # Check if all 26 characters are unique
    if len(set(key.lower())) != 26:
        return False
    
    return True

def main():
    while True:
        print("\nSubstitution Cipher Program")
        print("1. Encode Text")
        print("2. Decode Text")
        print("3. Exit")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1 or choice == 2:
            text = input("\nEnter The Text: ")
            key = input("Enter The Key (26 Unique Characters): ")
            
            if not isValidKey(key):
                print("Invalid Key! The Key Must Have 26 Unique Alphabetic Characters!")
                continue
            
            if choice == 1:
                print("\nEncoded Text:", encode(text, key))
            else:
                print("\nDecoded Text:", decode(text, key))
        elif choice == 3:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Choose Again!")

if __name__ == "__main__":
    main()
