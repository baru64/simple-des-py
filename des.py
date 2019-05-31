#!/usr/bin/python3
import argparse
import sys

ip_array = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
fp_array = [
    40, 8,  48, 16, 56, 24, 64, 32,
    39, 7,  47, 15, 55, 23, 63, 31,
    38, 6,  46, 14, 54, 22, 62, 30,
    37, 5,  45, 13, 53, 21, 61, 29,
    36, 4,  44, 12, 52, 20, 60, 28,
    35, 3,  43, 11, 51, 19, 59, 27,
    34, 2,  42, 10, 50, 18, 58, 26,
    33, 1,  41, 9,  49, 17, 57, 25
]
p_array = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]
expansion_array = [
    32, 1,  2,  3,  4,  5,
     4, 5,  6,  7,  8,  9,
     8, 9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
permutation_array = [
    16,  7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26,  5, 18, 31, 10,
     2,  8, 24, 14, 32, 27,  3,  9,
    19, 13, 30,  6, 22, 11,  4, 25
]
parity_drop = [
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4
]
key_rotation = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 
]
compression_array = [
    14, 17, 11, 24,  1,  5,  3, 28,
    15,  6, 21, 10, 23, 19, 12,  4,
    26,  8, 16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]
s_box_array = [
[
    14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
    4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
    15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
],
[
    15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
    3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
    0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3,  2, 15,
    13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
],
[
    10, 0, 9, 14, 6, 3, 15, 5 , 1, 13, 12, 7, 11, 4, 2, 8,
    13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
    13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
    1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 
],
[
    7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
    13, 8, 11, 5, 6, 15, 0, 3, 4 , 7, 2, 12, 1, 10, 14, 9,
    10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
    3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
],
[
    2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
    14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
    4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
    11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4,  5, 3
],
[
    12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
    10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
    9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4 , 10, 1, 13, 11, 6,
    4, 3, 2, 12, 9,  5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 
],
[
    4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
    13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
    1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8 , 0, 5, 9, 2,
    6, 11, 13, 8 , 1, 4, 10, 7, 9, 5 , 0, 15, 14, 2, 3, 12
],
[
    13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
    1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
    7, 11, 4 , 1, 9, 12, 14, 2, 0 , 6, 10, 13, 15, 3, 5, 8,
    2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
],
]

class des():

    def __init__(self, key=None):
        self.key = key
        self.current_key = None

    def _permutation(self, src_block, array):
        new_block = [0]*len(array)
        for i, v in enumerate(array):
            new_block[i] = src_block[v-1]
        return new_block

    def _s_box(self, src_array, n):
        row = int(src_array[0] + src_array[5], 2)
        col = int("".join(x for x in src_array[1:5]), 2)
        return s_box_array[n][row*16+col]
    
    def _fourbits2arr(self, bits):
        bits = bin(bits)[2:]
        if len(bits) < 4:
            bits = '0'*(4-len(bits)) + bits
        return [x for x in bits]

    def _bitlist_xor(self, a, b):
        c = a.copy()
        for j, v in enumerate(b):
            c[j] = str(int(c[j]) ^ int(v))
        return c
        
    def encrypt_block(self, src_block):
        block = self._permutation(src_block, ip_array)
        self.current_key = self._permutation(self.key, parity_drop)
        left = block[:32]
        right = block[32:]

        for i in range(16):
            exp_right = self._permutation(right, expansion_array)
            subkey = self._key_round(i)
            exp_right = self._bitlist_xor(exp_right, subkey) 

            nar_right = []
            for k in range(8):
                bits = self._s_box(exp_right[k*6:k*6+6], k)
                nar_right += self._fourbits2arr(bits)
            nar_right = self._permutation(nar_right, p_array)
            
            new_right = self._bitlist_xor(left, nar_right)
            left = right
            right = new_right
        
        block = right + left
        block = self._permutation(block, fp_array)
        return block

    def _key_round(self, n):
        left = self.current_key[:28]
        right = self.current_key[28:]
        
        left = left[key_rotation[n]:] + left[:key_rotation[n]]
        right = right[key_rotation[n]:] + right[:key_rotation[n]]
        
        self.current_key = left+right
        compressed = self._permutation(self.current_key, compression_array)
        return compressed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple DES implementation")
    parser.add_argument('-k', '--key-hex', default="", help='Pass key in hex')
    parser.add_argument('-f', '--key-filename', default="",
                        help='Pass binary file with key')
    parser.add_argument('--debug', action='store_true',
                        help='Debug mode, output in binary text')

    args = parser.parse_args()
    key = ""
    if args.key_hex:
        key = bin(int(args.key_hex, 16))[2:].zfill(64)
    elif args.key_filename:
        binary = b''
        with open(args.key_filename, "rb") as f:
            binary = f.read(8)
        key = "".join(bin(x)[2:].zfill(8) for x in binary)
    else:
        print('Error no key provided')
        sys.exit(1)
    
    cipher = des(key)
    while True:
        text = sys.stdin.read(8)
        if text == "" or text == "\n":
            break
        if len(text) < 8:
            text = text.ljust(8)
        block = "".join(bin(ord(x))[2:].zfill(8) for x in text)
        if args.debug:
            sys.stdout.write(
                    "".join(str(x) for x in cipher.encrypt_block(block))+'\n')
        else:
            encrypted = "".join(str(x) for x in cipher.encrypt_block(block))
            encrypted = [encrypted[n*8:n*8+8] for n in range(8)]
            for byte in encrypted:
                sys.stdout.write(chr(int(byte, 2)))
