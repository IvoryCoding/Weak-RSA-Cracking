########## IMPORTS ##########

import re
import string

########## FUNCTIONS ##########

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

########## CODE ##########

cipher_alphabet = {}

n = 3127
e = 3
cipher = str(113515182658265811321498451167914982025271645115181498635115314981016257612751742375399)

factors = prime_factors(n)

phi_n = (factors[0] - 1) * (factors[1] - 1)

j = 0
while True:
    if (j * e) % phi_n == 1:
        d = j
        break
    j += 1

### Creating a Cipher Ascii Table ###
for ch in list(string.printable):
    ct = (ord(ch) ** e) % n
    cipher_alphabet[ct] = ch

cracked_message = ''
letter_positions = {}
message_array = []
highest_position = 0

for key in cipher_alphabet:
    found_letter = list(re.finditer(str(key), cipher))

    if found_letter:
        letter_positions[key] = []

    for letter in found_letter:
        letter_positions[key].append(letter.span())

        cracked_message += cipher_alphabet[key]

        if highest_position < letter.end():
            highest_position = letter.end()

pos = 0
while pos != highest_position:
    for key in letter_positions:
        for letter_pos in letter_positions[key]:
            if letter_pos[0] == pos:
                message_array.append(cipher_alphabet[key])
                pos = letter_pos[1]

#print('\n=========== Basic Info ===========')
print(f'\nPrime Factors: {factors}')
print(f'Phi n: {phi_n}')
print(f'Private Key: {[d, phi_n]}')
print(f'Cipher Message: {cipher}\n')
#print('==================================\n')
print(f'            Cracking...\n')
#print('============ Cracking ============\n')
#print(f'Cipher Ascii Table: \n{cipher_alphabet}\n')
#print(f'Letters and Positions: \n{letter_positions}\n')
print(f'Cracked letters: {cracked_message}')
print(f'Message: {"".join(message_array)}\n')
#print('==================================\n')