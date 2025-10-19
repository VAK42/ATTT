#include <iostream>
#include <cctype>
using namespace std;

string encode(string text, int shift) {
  string result = "";
  for (int i = 0; i < text.length(); i++) {
    if (isupper(text[i]))
      result += char(int(text[i] + shift - 65) % 26 + 65);
    else if (islower(text[i]))
      result += char(int(text[i] + shift - 97) % 26 + 97);
    else
      result += text[i];
  }
  return result;
}

string decode(string ciphertext, int shift) {
  string result = "";
  for (int i = 0; i < ciphertext.length(); i++) {
    if (isupper(ciphertext[i]))
      result += char(int(ciphertext[i] - shift - 65 + 26) % 26 + 65);
    else if (islower(ciphertext[i]))
      result += char(int(ciphertext[i] - shift - 97 + 26) % 26 + 97);
    else
      result += ciphertext[i];
  }
  return result;
}

int main() {
  int shift;
  string text, choice;

  while (true) {
    cout << "\nCaesar Cipher Program\n";
    cout << "1. Encode Text\n";
    cout << "2. Decode Text\n";
    cout << "3. Exit\n";
    cout << "Enter Your Choice: ";
    cin >> choice;

    if (choice == "1" || choice == "2") {
      cout << "\nEnter The Text: ";
      cin.ignore();
      getline(cin, text);
      cout << "Enter The Shift Value: ";
      cin >> shift;

      if (choice == "1") {
        cout << "\nEncoded Text: " << encode(text, shift) << endl;
      } else {
        cout << "\nDecoded Text: " << decode(text, shift) << endl;
      }
    } else if (choice == "3") {
      cout << "Exiting Program...\n";
      break;
    } else {
      cout << "Invalid Choice! Please Choose Again!\n";
    }
  }
  return 0;
}
