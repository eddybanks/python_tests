from cryptography.fernet import Fernet

def fernet_key():
    key = Fernet.generate_key()
    f = Fernet(key)
    return f


def fernet_encryption(msg, f_key):
    token = f_key.encrypt(msg.encode())
    return token


def fernet_decryption(token, f_key):
    return f_key.decrypt(token)


def choices():
    print("Choose one of the following options")
    print("*" * 15)
    return input("1: Fernet Encryption, 2: Fernet Decryption, 0: Exit\n")


def manage_options(options, f):
    if options == '1':
        message = input("Enter the message to be encrypted: ")
        token = fernet_encryption(message, f)
        print(token)
    elif options == '2':
        d_token = input("Enter token to be decrypted: ")
        try:
            d_message = fernet_decryption(d_token.encode(), f)
            print(d_message.decode())
        except:
            print("haha")
        else:
            print("soso")


def encrypt_message():
    f = fernet_key()
    options = 2
    while(options != '0'):
        options = choices()
        manage_options(options, f)
        print()


encrypt_message()
