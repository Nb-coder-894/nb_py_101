from cryptography.fernet import Fernet

# Generate the key
key = Fernet.generate_key()

# Print it (or save it to a file)
print(key.decode())
