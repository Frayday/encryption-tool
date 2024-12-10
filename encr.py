import cryptography.fernet
import cryptography.hazmat.backends
import cryptography.hazmat.primitives.asymmetric
import cryptography.hazmat.primitives.serialization
import cryptography.hazmat.primitives
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Symmetric Encryption (Fernet)

def symmetric_encrypt(filepath, key):
    f = cryptography.fernet.Fernet(key)
    with open(filepath, 'rb') as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filepath + ".enc", 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(filepath)
    return filepath + ".enc"

def symmetric_decrypt(filepath, key):
    f = cryptography.fernet.Fernet(key)
    with open(filepath, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = f.decrypt(encrypted_data)
    filename = filepath.split(".enc")[0]
    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    os.remove(filepath)
    return filename

# Asymmetric Encryption (RSA) - Example with Key Generation
def generate_rsa_keys(filename_public, filename_private):
	key_pair = cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(
    	public_exponent=65537,
    	key_size=2048,
    	backend=cryptography.hazmat.backends.default_backend()
	)

	private_key = key_pair
	public_key = key_pair.public_key()


	pem = public_key.public_bytes(
    	encoding=cryptography.hazmat.primitives.serialization.Encoding.PEM,
    	format=cryptography.hazmat.primitives.serialization.PublicFormat.SubjectPublicKeyInfo
	)

	with open(filename_public, 'wb') as f:
		f.write(pem)


	pem = private_key.private_bytes(
    	encoding=cryptography.hazmat.primitives.serialization.Encoding.PEM,
    	format=cryptography.hazmat.primitives.serialization.PrivateFormat.TraditionalOpenSSL,
    	encryption_algorithm=cryptography.hazmat.primitives.serialization.NoEncryption()
	)


	with open(filename_private, 'wb') as f:
		f.write(pem)

def asymmetric_encrypt(filepath, public_key_path):


	with open(public_key_path, "rb") as key_file:
		public_key = cryptography.hazmat.primitives.serialization.load_pem_public_key(key_file.read(), cryptography.hazmat.backends.default_backend())


	with open(filepath, "rb") as file:
		data = file.read()

	encrypted_data = public_key.encrypt(data,None)


	with open(filepath+".enc", "wb") as encrypted_file:
	    encrypted_file.write(encrypted_data[0])


	return filepath + ".enc"



#GUI (Tkinter)

root = tk.Tk()
root.title("Custom Encryption Tool")


# Add Symmetric Encryption

# ... (rest of the code for asymmetric encryption and GUI elements)


root.mainloop()