#include <iostream>
using namespace std;

int modInverse(int a, int m) {
  for (int x = 1; x < m; x++) {
    if ((a * x) % m == 1) {
      return x;
    }
  }
  return -1;
}

int determinant(int keyMatrix[][3]) {
  int det = keyMatrix[0][0] * (keyMatrix[1][1] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][1]);
  det -= keyMatrix[0][1] * (keyMatrix[1][0] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][0]);
  det += keyMatrix[0][2] * (keyMatrix[1][0] * keyMatrix[2][1] - keyMatrix[1][1] * keyMatrix[2][0]);
  return det % 26;
}

void adjugate(int keyMatrix[][3], int adj[][3]) {
  adj[0][0] = keyMatrix[1][1] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][1];
  adj[0][1] = -(keyMatrix[0][1] * keyMatrix[2][2] - keyMatrix[0][2] * keyMatrix[2][1]);
  adj[0][2] = keyMatrix[0][1] * keyMatrix[1][2] - keyMatrix[0][2] * keyMatrix[1][1];
  adj[1][0] = -(keyMatrix[1][0] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][0]);
  adj[1][1] = keyMatrix[0][0] * keyMatrix[2][2] - keyMatrix[0][2] * keyMatrix[2][0];
  adj[1][2] = -(keyMatrix[0][0] * keyMatrix[1][2] - keyMatrix[0][2] * keyMatrix[1][0]);
  adj[2][0] = keyMatrix[1][0] * keyMatrix[2][1] - keyMatrix[1][1] * keyMatrix[2][0];
  adj[2][1] = -(keyMatrix[0][0] * keyMatrix[2][1] - keyMatrix[0][1] * keyMatrix[2][0]);
  adj[2][2] = keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0];
}

bool inverse(int keyMatrix[][3], int inverseMatrix[][3]) {
  int det = determinant(keyMatrix);
  det = (det + 26) % 26;
  int detInverse = modInverse(det, 26);
  if (detInverse == -1) {
    cout << "Inverse Doesn't Exist For The Given Matrix (Determinant Is 0 Modulo 26)!\n";
    return false;
  }
  int adj[3][3];
  adjugate(keyMatrix, adj);
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      inverseMatrix[i][j] = (adj[i][j] * detInverse) % 26;
      if (inverseMatrix[i][j] < 0) {
        inverseMatrix[i][j] += 26;
      }
    }
  }
  return true;
}

void getKeyMatrix(string key, int keyMatrix[][3]) {
  int k = 0;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      keyMatrix[i][j] = (key[k] - 'A') % 26;
      k++;
    }
  }
}

void encrypt(int cipherMatrix[][1], int keyMatrix[][3], int messageVector[][1]) {
  int x, i, j;
  for (i = 0; i < 3; i++) {
    for (j = 0; j < 1; j++) {
      cipherMatrix[i][j] = 0;
      for (x = 0; x < 3; x++) {
        cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j];
      }
      cipherMatrix[i][j] = cipherMatrix[i][j] % 26;
    }
  }
}

void decrypt(int cipherMatrix[][1], int inverseMatrix[][3], int messageVector[][1]) {
  int x, i, j;
  for (i = 0; i < 3; i++) {
    for (j = 0; j < 1; j++) {
      cipherMatrix[i][j] = 0;
      for (x = 0; x < 3; x++) {
        cipherMatrix[i][j] += inverseMatrix[i][x] * messageVector[x][j];
      }
      cipherMatrix[i][j] = cipherMatrix[i][j] % 26;
    }
  }
}

void HillCipher(string message, string key, bool encrypting = true) {
  int keyMatrix[3][3];
  getKeyMatrix(key, keyMatrix);

  int messageVector[3][1];
  for (int i = 0; i < 3; i++) {
    messageVector[i][0] = (message[i] - 'A');
  }

  int cipherMatrix[3][1];
  if (encrypting) {
    encrypt(cipherMatrix, keyMatrix, messageVector);
  } else {
    int inverseMatrix[3][3];
    if (!inverse(keyMatrix, inverseMatrix)) {
      return;
    }
    decrypt(cipherMatrix, inverseMatrix, messageVector);
  }

  string resultText;
  for (int i = 0; i < 3; i++) {
    resultText += (char)(cipherMatrix[i][0] + 'A');
  }

  cout << (encrypting ? "Ciphertext: " : "Plaintext: ") << resultText << endl;
}

int main() {
  int choice;
  string message, key;

  while (true) {
    cout << "\nHill Cipher Program\n";
    cout << "1. Encrypt Text\n";
    cout << "2. Decrypt Text\n";
    cout << "3. Exit\n";
    cout << "Enter Your Choice: ";
    cin >> choice;

    switch (choice) {
    case 1:
      cout << "Enter The Message (3 Characters): ";
      cin >> message;
      cout << "Enter The Key (9 Characters): ";
      cin >> key;
      if (message.length() != 3 || key.length() != 9) {
        cout << "Message Must Be 3 Characters & Key Must Be 9 Characters Long!\n";
      } else {
        HillCipher(message, key, true);
      }
      break;
    case 2:
      cout << "Enter The Message (3 Characters): ";
      cin >> message;
      cout << "Enter The Key (9 Characters): ";
      cin >> key;
      if (message.length() != 3 || key.length() != 9) {
        cout << "Message Must Be 3 Characters & Key Must Be 9 Characters Long!\n";
      } else {
        HillCipher(message, key, false);
      }
      break;
    case 3:
      cout << "Exiting Program...\n";
      return 0;
    default:
      cout << "Invalid Choice! Please Choose Again!\n";
    }
  }
}
