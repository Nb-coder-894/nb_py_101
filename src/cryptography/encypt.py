from cryptography.fernet import Fernet

key = b'4CGnk5hCgqlauPJxnbxgrbb46AobL-eJSq6-bwVw1Ic='
cipher = Fernet(key)

encrypted_info = b"""

"""

encrypted = cipher.encrypt(encrypted_info)

print(encrypted)