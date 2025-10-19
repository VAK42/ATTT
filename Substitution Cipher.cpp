#include <iostream>
#include <map>
#include <string>
#include <cctype>
using namespace std;

string encode(string plainTxt, string key) {
  string cipherTxt;
  string lowerLetrs = "abcdefghijklmnopqrstuvwxyz";
  string upperLetrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  map < char, char > dict1;

  for (int i = 0; i < lowerLetrs.length(); i++) {
    dict1[lowerLetrs[i]] = key[i];
    dict1[upperLetrs[i]] = toupper(key[i]);
  }

  for (char & c: plainTxt) {
    if (dict1.find(c) != dict1.end()) {
      cipherTxt += dict1[c];
    } else {
      cipherTxt += c;
    }
  }

  return cipherTxt;
}

string decode(string cipherTxt, string key) {
  string decryptTxt;
  string lowerLetrs = "abcdefghijklmnopqrstuvwxyz";
  string upperLetrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  map < char, char > dict2;

  for (int i = 0; i < lowerLetrs.length(); i++) {
    dict2[key[i]] = lowerLetrs[i];
    dict2[toupper(key[i])] = upperLetrs[i];
  }

  for (char & c: cipherTxt) {
    if (dict2.find(c) != dict2.end()) {
      decryptTxt += dict2[c];
    } else {
      decryptTxt += c;
    }
  }

  return decryptTxt;
}

int main() {
  int choice;
  string text, key;

  while (true) {
    cout << "\nSubstitution Cipher Program\n";
    cout << "1. Encode Text\n";
    cout << "2. Decode Text\n";
    cout << "3. Exit\n";
    cout << "Enter Your Choice: ";
    cin >> choice;

    if (choice == 1 || choice == 2) {
      cout << "\nEnter The Text: ";
      cin.ignore();
      getline(cin, text);
      cout << "Enter The Substitution Key (26 Characters For Alphabet): ";
      cin >> key;

      if (key.length() != 26) {
        cout << "Invalid Key Length! The Key Must Have 26 Characters!\n";
        continue;
      }

      if (choice == 1) {
        cout << "\nEncoded Text: " << encode(text, key) << endl;
      } else {
        cout << "\nDecoded Text: " << decode(text, key) << endl;
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
