from hashlib import sha256
import binascii


def get_bip39_words_list():
    lines = None
    # downloaded from https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt
    with open('./english.txt') as file:
        lines = [line.rstrip() for line in file]
    assert(len(lines) == 2048)
    return lines


def main():
    bip39_words_list = get_bip39_words_list()

    while True:
        try:
            entropy = input('Enter your own bits of entropy. A sequence of 128 (for 12 words) or 256 (for 24 words - RECOMMENDED) characters made of "0" and "1":\n').strip()
        except KeyboardInterrupt:
            return

        if not all(char in '01' for char in entropy):
            print('\nERROR: entropy invalid. Insert a sequence of only 0 and 1\n')
            continue

        if len(entropy) != 128 and len(entropy) != 256:
            print('\nERROR: invalid entropy length. Provided {} bits of entropy. 128 or 256 bits must be provided\n'.format(len(entropy)))
            continue

        break

    hexstr = "{0:0>4X}".format(int(entropy,2)) 
    data = binascii.a2b_hex(hexstr)
    hs = sha256(data).hexdigest()

    chars_for_checksum = None
    if len(entropy) == 256:
        chars_for_checksum = 2
    elif len(entropy) == 128:
        chars_for_checksum = 1

    last_bits = ''.join([ str(bin(int(hs[i], 16))[2:].zfill(4)) for i in range(0, chars_for_checksum) ])
    entropy += last_bits

    bits_per_word = 11
    splitted = [entropy[i:i+bits_per_word] for i in range(0, len(entropy), bits_per_word)]
    words = [ bip39_words_list[int(i, 2)] for i in splitted ]
    
    print('\nSEED GENERATED:\n\n{}\n'.format(' '.join(words)))
    

if __name__ == "__main__":
    main()
