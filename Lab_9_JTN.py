#Jackson Nichols

def encode_password(password):
    new_pw = []

    for char in password:
        val = ord(char) + 3
        new_pw.append(chr(val))
    final_pw = ''.join(new_pw)
    return final_pw





