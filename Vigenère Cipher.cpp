#include <iostream>
#include <string>
using namespace std;

string generateKey(string str, string key) {
  int x = str.size();
  for (int i = 0;; i++) {
    if (x == i)
      i = 0;
    if (key.size() == str.size())
      break;
    key.push_back(key[i]);
  }
  return key;
}

string encode(string str, string key) {
  string cipherText;
  for (int i = 0; i < str.size(); i++) {
    if (isalpha(str[i])) {
      char x = (toupper(str[i]) + toupper(key[i])) % 26;
      x += 'A';
      cipherText.push_back(x);
    } else {
      cipherText.push_back(str[i]);
    }
  }
  return cipherText;
}

string decode(string cipherText, string key) {
  string origText;
  for (int i = 0; i < cipherText.size(); i++) {
    if (isalpha(cipherText[i])) {
      char x = (toupper(cipherText[i]) - toupper(key[i]) + 26) % 26;
      x += 'A';
      origText.push_back(x);
    } else {
      origText.push_back(cipherText[i]);
    }
  }
  return origText;
}

int main() {
  int choice;
  string text, key;

  while (true) {
    cout << "\nVigenère Cipher Program\n";
    cout << "1. Encode Text\n";
    cout << "2. Decode Text\n";
    cout << "3. Exit\n";
    cout << "Enter Your Choice: ";
    cin >> choice;

    if (choice == 1 || choice == 2) {
      cout << "\nEnter The Text: ";
      cin.ignore();
      getline(cin, text);
      cout << "Enter The Key: ";
      cin >> key;

      if (key.length() != text.length()) {
        cout << "Key Length Must Match The Text Length!\n";
        continue;
      }

      string keyGenerated = generateKey(text, key);

      if (choice == 1) {
        cout << "\nEncoded Text: " << encode(text, keyGenerated) << endl;
      } else {
        cout << "\nDecoded Text: " << decode(text, keyGenerated) << endl;
      }
    } else if (choice == 3) {
      cout << "Exiting Program...\n";
      break;
    } else {
      cout << "Invalid Choice! Please Choose Again!\n";
    }
  }
  return 0;
}
