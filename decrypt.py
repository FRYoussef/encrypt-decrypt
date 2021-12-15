import getpass
from cryptography.fernet import Fernet

if __name__ == '__main__':
    file_name: str = input(f'Introduce file path: ')
    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    password = getpass.getpass('Introduce the key to decrypt: ')
    password = bytes(password, 'utf-8')
    f = Fernet(password)

    decrypted_data = f.decrypt(encrypted_data)
    print(decrypted_data.decode('utf-8'))
