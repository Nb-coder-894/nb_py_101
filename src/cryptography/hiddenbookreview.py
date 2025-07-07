from cryptography.fernet import Fernet
# You only need to generate this key once and keep it secret
key = b'4CGnk5hCgqlauPJxnbxgrbb46AobL-eJSq6-bwVw1Ic='  # Use Fernet.generate_key() to get this

cipher = Fernet(key)

# Encrypted book report (encrypt your text once)
encrypted_report = b"gAAAAABoa0ZDpfE6ggLMDW19gGNWFG7OgXvJXGpNpO1-3ieE6ScRgNw20u8VhgdrVAhbMDhaFkVRPI-nbefeLuyV46rzEFbbZxrDH7wATPjc0yZEJvhft4Js24ZYLz1jB5lHm99b2V63r-kd8j_mF5_Nqba9vZojfi1IOq9mZc6-VDukkGhB3q1TslBxheW5MPB5e3j4a8tW'"  # encrypted bytes

def main():
    password = float(input("Enter password: "))
    if password == 2013.2012201120102009200820072005:
        # Decrypt and print
        decrypted = cipher.decrypt(encrypted_report).decode()
        print(decrypted)
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
