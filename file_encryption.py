import os
import base64
import secrets
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


#  Crypto Helpers


def derive_key(password: str, salt: bytes, iterations: int = 390000) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


#  Encryption


def encrypt_file():
    if not enc_file.get() or not enc_pass.get():
        messagebox.showerror("Error", "Select file and enter password")
        return

    try:
        with open(enc_file.get(), "rb") as f:
            data = f.read()

        salt = secrets.token_bytes(16)
        key = derive_key(enc_pass.get(), salt)
        encrypted = Fernet(key).encrypt(data)

        filename = os.path.basename(enc_file.get()).encode()
        out_path = enc_file.get() + ".enc"

        with open(out_path, "wb") as f:
            f.write(b"FILE")
            f.write(salt)
            f.write(len(filename).to_bytes(2, "big"))
            f.write(filename)
            f.write(encrypted)

        messagebox.showinfo("Success", f"Encrypted:\n{out_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


#  Decryption


def decrypt_file():
    if not dec_file.get() or not dec_pass.get():
        messagebox.showerror("Error", "Select file and enter password")
        return

    try:
        with open(dec_file.get(), "rb") as f:
            if f.read(4) != b"FILE":
                raise ValueError("Invalid encrypted file")

            salt = f.read(16)
            name_len = int.from_bytes(f.read(2), "big")
            original_name = f.read(name_len).decode()
            encrypted = f.read()

        key = derive_key(dec_pass.get(), salt)
        decrypted = Fernet(key).decrypt(encrypted)

        out_path = os.path.join(os.path.dirname(dec_file.get()), original_name)

        with open(out_path, "wb") as f:
            f.write(decrypted)

        messagebox.showinfo("Success", f"Decrypted:\n{out_path}")

    except Exception:
        messagebox.showerror("Error", "Wrong password or corrupted file")


#  GUI Helpers


def browse_enc():
    path = filedialog.askopenfilename()
    if path:
        enc_file.set(path)


def browse_dec():
    path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
    if path:
        dec_file.set(path)


#  GUI Layout

root = tk.Tk()
root.title(" File Encryption Tool")
root.geometry("520x480")
root.resizable(False, False)

enc_file = tk.StringVar()
enc_pass = tk.StringVar()
dec_file = tk.StringVar()
dec_pass = tk.StringVar()

tk.Label(root, text="File Encryption", font=("Arial", 16, "bold")).pack(pady=10)

#  Encryption Frame

enc_frame = tk.LabelFrame(root, text="🔐 Encrypt File", padx=15, pady=10)
enc_frame.pack(fill="x", padx=15, pady=10)

tk.Entry(enc_frame, textvariable=enc_file, width=50).pack()
tk.Button(enc_frame, text="Browse File", command=browse_enc).pack(pady=5)

tk.Label(enc_frame, text="Password").pack()
tk.Entry(enc_frame, textvariable=enc_pass, show="*", width=30).pack()

tk.Button(enc_frame, text="Encrypt", width=20, command=encrypt_file).pack(pady=8)

#  Decryption Frame

dec_frame = tk.LabelFrame(root, text="🔓 Decrypt File", padx=15, pady=10)
dec_frame.pack(fill="x", padx=15, pady=10)

tk.Entry(dec_frame, textvariable=dec_file, width=50).pack()
tk.Button(dec_frame, text="Browse .enc File", command=browse_dec).pack(pady=5)

tk.Label(dec_frame, text="Password").pack()
tk.Entry(dec_frame, textvariable=dec_pass, show="*", width=30).pack()

tk.Button(dec_frame, text="Decrypt", width=20, command=decrypt_file).pack(pady=8)

tk.Label(root, text="Supports all file types", fg="gray").pack(pady=5)

root.mainloop()
