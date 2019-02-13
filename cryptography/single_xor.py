import sys

def xor(message, char):
    result = ''
    for c in message:
        result += chr(ord(c) ^ ord(char))
    return result

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 single_xor.py [message] [character]')
    else:
        print(xor(sys.argv[1], sys.argv[2]))
