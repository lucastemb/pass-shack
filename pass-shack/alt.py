from argon2 import PasswordHasher
ph = PasswordHasher(time_cost = 2, memory_cost = 102400, parallelism = 10, hash_len = 16 , sal_len = 16, encoding = "utf-8", type = ID)
password = input()
hash = ph.hash(password)
print(hash)
