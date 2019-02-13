import sys

def shift_char(char, shift):
    # keep track of casing
    isupper = 1 if char.isupper() else 0
    # convert to lower case and make 0-indexed
    result = ord(char.lower()) - ord('a')
    shift = ord(shift.lower()) - ord('a')
    # add shift
    result = (result + shift) % 26
    # convert back to character
    result = chr(result + ord('a'))
    if isupper:
        result = result.upper()
    return result

def caesar(message, shift):
    result = ''
    # for each character,
    for char in message:
        if char.isalpha():  # if it's in [a-zA-Z], shift it
            result += shift_char(char, shift)
        else:
            result += char  # otherwise just add it
    return result
    


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 caesar.py [message] [character]')
    else:
        print(caesar(sys.argv[1], sys.argv[2]))
