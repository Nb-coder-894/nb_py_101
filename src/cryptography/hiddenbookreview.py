from cryptography.fernet import Fernet
# You only need to generate this key once and keep it secret
key = b'bQvdv_OcaTVfe0vjFPvud9qROKHsGjyI87ysvoXlRAc='  # Use Fernet.generate_key() to get this

cipher = Fernet(key)

# Encrypted book report (encrypt your text once)
encrypted_report = b'gAAAAABoa0TaeklyRnE7tm90myCL1YMl5Ne3oCDkafcBkZy-n_vrePp7L3BETwxITqr5O6BUOrrSiZmLjqXrYX80EU8tnA0UCoFsvg2nJl4FaN3zhKbjwBBlCRH28NO2uEHYRxCX9NjWmjkjQurr6kmTG719dWR86AppU13KZVtEsqH2n4aPMqEnJY98deE-yLqGNbZUdlynb__x9SCCU9kGb4B2RnaUjyQrjNGZKIOxC7Helh1fanAJdEHmKtRa67QQ618n8deHsxRBtZQ841lw_fmZjjVIT48bXLv4KvoT790kDHGHiEYJ6dcqvoENhze2yLRrKy1LxiCVsZEe4sZDH-qcVLYIi8SP1NBVFpaVLbSvfxFcM_FxyPdUWUJlD-P7PrZ5a__OS6_S6dGzeehUIcyp8_DV6pjbDd5Ka85eRDiBvR2dOGc'  # encrypted bytes

def main():
    password = input("Enter password: ").lower()
    if password == "sunetro":
        # Decrypt and print
        decrypted = cipher.decrypt(encrypted_report).decode()
        print(decrypted)
    else:
        print("ERROR 400")

if __name__ == "__main__":
    main()
