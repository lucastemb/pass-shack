from pyargon2 import hash

masterpass = input()
platform = input()

def login(masterpass, platform):
    hashedpass = hash(masterpass, platform)
    print(hashedpass)

print(login(masterpass, platform))