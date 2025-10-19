#include <iostream>
#include <string>
using namespace std;

const int a = 17;
const int b = 20;

string encode(string msg) {
  string cipher = "";
  for (int i = 0; i < msg.length(); i++) {
    if (isalpha(msg[i])) {
      if (isupper(msg[i]))
        cipher += (char)((((a * (msg[i] - 'A')) + b) % 26) + 'A');
      else
        cipher += (char)((((a * (msg[i] - 'a')) + b) % 26) + 'a');
    } else {
      cipher += msg[i];
    }
  }
  return cipher;
}

string decode(string cipher) {
  string msg = "";
  int aInv = 0;
  int flag = 0;

  for (int i = 0; i < 26; i++) {
    flag = (a * i) % 26;
    if (flag == 1) {
      aInv = i;
    }
  }

  for (int i = 0; i < cipher.length(); i++) {
    if (isalpha(cipher[i])) {
      if (isupper(cipher[i]))
        msg += (char)(((aInv * ((cipher[i] - 'A' - b + 26) % 26)) % 26) + 'A');
      else
        msg += (char)(((aInv * ((cipher[i] - 'a' - b + 26) % 26)) % 26) + 'a');
    } else {
      msg += cipher[i];
    }
  }
  return msg;
}

int main(void) {
  int choice;
  string text;

  while (true) {
    cout << "\nAffine Cipher Program\n";
    cout << "1. Encode Text\n";
    cout << "2. Decode Text\n";
    cout << "3. Exit\n";
    cout << "Enter Your Choice: ";
    cin >> choice;

    if (choice == 1 || choice == 2) {
      cout << "\nEnter The Text: ";
      cin.ignore();
      getline(cin, text);

      if (choice == 1) {
        cout << "\nEncoded Text: " << encode(text) << endl;
      } else {
        cout << "\nDecoded Text: " << decode(text) << endl;
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
