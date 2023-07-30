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

alphabet_list = list(string.ascii_letters) + [' ', '!', '.', '?']

print(f'{alphabet_list}')

n = 3127
e = 3
cipher = str(113515182658265811321498451167914982025271645115181498635115314981744514512716399)

factors = prime_factors(n)

phi_n = (factors[0] - 1) * (factors[1] - 1)

j = 0
while True:
    if (j * e) % phi_n == 1:
        d = j
        break
    j += 1

### Decrypting a longer ciphered message ###

n_len = len(str(n))

rep_numbers = re.findall('[0-9]{%i}'%n_len, cipher)
biggest_count_num = 0

for num in rep_numbers:
    if (cipher.count(num) > 1):
        if cipher.count(str(biggest_count_num)) < cipher.count(str(num)):
            biggest_count_num = num

cipher_words = cipher.split(biggest_count_num)

cracked_words = []

for word in cipher_words:
    first_word = re.findall('[0-9]{%i}'%n_len, word)

    letters_to_words = []
    for digits_4 in first_word:
        mes = (int(digits_4) ** d) % n
        letters_to_words.append(chr(mes))

    cracked_words.append(letters_to_words)
    
print('=========== Basic Info ===========')
print(f'\nPrime Factors: {factors}\n')
print(f'Phi n: {phi_n}\n')
print(f'Private Key: {[d, phi_n]}\n')
print(f'Cipher Message: {cipher}\n')
print('==================================\n')

print('============ Cracking ============')
print(f'\nHighest Count Number: {biggest_count_num}\n')
print(f'Chipher Words Array: {cipher_words}\n')
print(f'Decrypted words: {cracked_words}\n')
print(f'Decrypted Message: \n')
print('==================================')