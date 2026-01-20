# 🔐 File-Encryption-GUI-Tool

A Python-based **File Encryption** that allows users to **securely encrypt any file** using a password and later **decrypt it back to its original form**.

This project uses **Fernet symmetric encryption**, **PBKDF2-HMAC key derivation**, and a clean **Tkinter-based graphical interface**, making it simple, safe, and beginner-friendly.

---

## 🧱 Project Structure

```bash
File-Encryption-GUI-Tool/
│
├── file_encryption.py       # Main GUI application
└── README.md                # Project documentation
```

---

## ✨ Features

## 🔐 File Encryption

- Encrypts **any file type** (video, image, audio, documents, etc.)
- Uses **Fernet (AES-128 authenticated encryption)**
- Password-based key derivation using **PBKDF2-HMAC (SHA256, 390,000 iterations)**
- Generates a secure encrypted file with `.enc` extension
- Stores metadata safely using a **MAGIC header**

## 🔓 File Decryption

- Decrypts `.enc` encrypted files back to original format
- Restores the **original file name and content**
- Detects invalid or corrupted encrypted files
- Protects against wrong password usage

## 🖥 GUI Highlights

- Simple and clean **Tkinter interface**
- Separate sections for **Encryption and Decryption**
- File browser support for easy file selection
- Password-protected operations
- Proper success & error dialogs
- **Supports all file formats**

---

## 🛠 Technologies Used

| Technology                             | Role                        |
| -------------------------------------- | --------------------------- |
| **Python 3**                           | Core language               |
| **Tkinter**                            | GUI framework               |
| **cryptography (Fernet + PBKDF2HMAC)** | Encryption & key derivation |
| **secrets**                            | Secure salt generation      |
| **base64 / os**                        | Binary & file handling      |

---
## 📌 Requirements

Make sure you install required dependencies:

```bash
pip install cryptography 
```

Standard libraries like `secrets`, `tkinter`, `base64`, and `struct` are already included with Python.

---

## ▶️ How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/ShakalBhau0001/File-Encryption-GUI-Tool.git
```

**2. Enter the project folder:**

```bash
cd File-Encryption-GUI-Tool
```

**3. Run the GUI:**

```bash
python file_encryption.py
```

---

## 📁 Supported File Format

- **Input:** Any file type
- **Encrypted Output:** `.enc`
- **Decrypted Output:** Original file format restored

> ⚠️ Encrypted files without a valid MAGIC header will be rejected.

---

## ⚙️ How It Works

**1️⃣ Key Derivation**

- Password → PBKDF2-HMAC(SHA256, 390,000 iterations) → 32-byte key → Fernet key

**2️⃣ Encryption**

- File data encrypted using Fernet
- Encrypted file structure:
    ```bash
    [FILE][16-byte salt][filename length][original filename][encrypted data]
    ```

**3️⃣ Decryption**

- Validates MAGIC header
- Extracts salt & filename
- Re-derives encryption key
- Decrypts file back to original format

---

## ⚠️ Common Errors

- **Wrong password** → Decryption fails
- **Invalid file** → MAGIC header missing
- **Corrupted file** → Decryption error
- **Renamed `.enc` file** → Still works (metadata stored internally)

---

## 🌟 Future Enhancements

- Drag & drop file support
- Folder encryption
- Image capacity calculator
- Progress bar for large files
- Dark mode UI

---

## 📦 Extended Version

This repository focuses on a specific steganography technique and is designed
**for learning and experimentation**.

For a **more advanced and combined implementation** that includes
image and audio steganography with file encryption support, refer to:

 🔗 **[StegaVault-GUI](https://github.com/ShakalBhau0001/StegaVault-GUI)**

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.
It is not designed to provide real-world secure file communication.

---

## 🪪 Author

> **Creator: Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---
