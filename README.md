# MSGCRYPT 🔐

MSGCRYPT is a simple desktop encryption note-taking application built with Python.  
It allows users to write messages, encrypt/decrypt them using Fernet encryption, and save/load notes locally.

---

## ✨ Features

- 🔐 Encrypt and decrypt messages using Fernet (AES-based encryption)
- 📝 Built-in text editor (CustomTkinter UI)
- 💾 Save notes automatically as message1.txt, message2.txt, etc.
- 📂 Load saved notes into the editor
- 🧹 Clear text instantly
- 🧭 Sidebar-based modern UI layout
- ⚙️ Setup batch file for easy installation of dependencies

---

## 🛠️ Technologies Used

- Python 3
- CustomTkinter (GUI framework)
- Cryptography (Fernet encryption)
- OS module (file handling)
- Tkinter filedialog (file loading)

---

## 📦 Installation

### 1. Clone the repository

git clone https://github.com/jbrown-js/msgcrypt.git
cd msgcrypt

---

### 2. Install dependencies

You can use the included setup script:

install.bat

---

### 3. Generate KEY

The setup file automatically generates you a key so you can skip this step if you used setup.bat

---

## 🚀 How to Run

python main.py

---

## 🔑 Encryption Key Setup

MSGCRYPT uses a Fernet key stored locally in key.key.

- A key is generated automatically if missing (via setup or keygen script)
- This key is required to encrypt and decrypt messages
- Do NOT delete or modify this file unless you want to reset encrypted data

---

## 📁 Project Structure

msgcrypt/
│
├── main.py        # Main application (GUI)
├── keyGen.py      # Key generator script
├── logo.txt       # Ascii Logo for Setup
├── setup.bat      # Setup script

---

## ⚠️ Notes

- If the key is changed or deleted, previously encrypted messages cannot be decrypted
- This project is intended for educational purposes
- Not intended for high-security production use

---

## 👨‍💻 Author

jbrown-js

---

## 📜 License

This project is open-source and free to use for learning purposes.
