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

n = 3127
e = 3
cipher = 113515182658265811321498451167914982025271645115181498635115314981744514512716399

factors = prime_factors(n)

phi_n = (factors[0] - 1) * (factors[1] - 1)

j = 0
while True:
    if (j * e) % phi_n == 1:
        d = j
        break
    j += 1

mes = (cipher ** d) % n

print(f'\nPrime Factors: {factors}\n')
print(f'Phi n: {phi_n}\n')
print(f'Private Key: {[d, phi_n]}\n')
print(f'Cipher Message: {cipher}')
print(f'Decrypted Message: {mes}\n')