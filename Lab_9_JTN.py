#Jackson Nichols

def encode_password(password):
    new_pw = []
    for char in password:
        val = ord(char) + 3
        new_pw.append(chr(val))
    final_pw = ''.join(new_pw)
    return final_pw

def decode_password(password)





run = True

def main():
    while run:
        print('1. Encode\n2. Decode\n3. Quit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            pw = input('Enter your password: ')
            new_pw = encode_password(pw)
            print(f'Your password is: {new_pw}')

        if choice == 2:
            pw = input('Enter your encoded password: ')
            new_pw = decode_password(pw)
            print(f'Your password is: {new_pw}')

        if choice == 3: run = False










