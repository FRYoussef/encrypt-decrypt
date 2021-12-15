from cryptography.fernet import Fernet
import getpass

def write_encrypted(encrypted, file_name: str) -> None:
    with open (file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def encrypt_file(key) -> None:
    file_name: str = input(f'Introduce file path: ')

    with open(file_name, 'rb') as original_file:
        original = original_file.read()

    encrypted = key.encrypt(original)
    write_encrypted(encrypted, f'{file_name}_encrypted')


def encrypt_data(key) -> None:
    data: str = ''
    print('\nWrite the text you want to encrypt. To end the text input write \"!end!\" and press enter.\n')
    line: str = input("... ")
    while line != "!end!":
        data += line
        data += "\n"
        line = input("... ")

    file_name: str = input(f'\nIntroduce file name to store it: ')
    data = bytes(data, 'utf-8')
    encrypted = key.encrypt(data)
    write_encrypted(encrypted, file_name)


if __name__ == '__main__':
    in_file: str = input(f'Encrypt file (y/n): ')
    while in_file not in ['y', 'n']:
        in_file: str = input(f'Encrypt file (y/n): ')

    generate: str = input('Do you want to generate the encryptation key? (y/n): ')
    while generate not in ['y', 'n']:
        generate: str = input(f'Do you want to generate the encryptation key? (y/n): ')

    if generate == 'y':
        key = Fernet.generate_key()
    else:
        key = getpass.getpass('Introduce the encryptation key: ')
        key = bytes(key, 'utf-8')

    f = Fernet(key)

    if in_file == 'y':
        encrypt_file(key=f)
    else:
        encrypt_data(key=f)

    if generate == 'y':
        print(f'\nYour encryptation key is:\n\n{key.decode("utf-8")}\n')
