from database import insert_hashed_masterpass
from cryption import * 
def add_master_pass():
    masterpass = input("Master Password: ")
    confirm_masterpass = input("Re-type Master Password: ")
    if (masterpass != confirm_masterpass):
        print("\nAn error has occured:\nMaster password confirmation does not match.\n")
        add_master_pass()
    else: 

        master_hint = input("\nMaster Password Hint (optional): ")
        insert_hashed_masterpass(masterpass, AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').encrypt(master_hint))
        

    
def add_master_pass_wrapper():
    print('''
The master password is the password you use to access your vault.
It is very important that you do not forget your master password.
There is no way to recover the password in the event that you forget it.
    ''') 
    add_master_pass()

    
