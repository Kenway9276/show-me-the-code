import random, string

f = open('promo_code.txt', 'w')
for j in range(200):
    chars = string.digits + string.ascii_uppercase
    chosen_char = [random.choice(chars) for i in range(12)]
    f.write(''.join(chosen_char) + '\n')
f.close()

