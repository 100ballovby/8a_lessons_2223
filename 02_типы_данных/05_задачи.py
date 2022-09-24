import random as r

r_int = r.randint(100, 999)

hundreds = r_int // 100
tens = r_int % 100 // 10
units = r_int % 10

print(r_int, hundreds + tens + units)


