from cryptography.fernet import Fernet
key = Fernet.generate_key() #generate key using fernet.generate_key for purpose of encryption and decryption
with open("password_key" , "wb") as my_keys:  # this opens password_key and write bainary because the genrated key is in bytes and gives it a nickname my_keys
    my_keys.write(key) #this write the key we generated uisng fernet to my_keys which is the nickname of password_key

print(f"keys: {my_keys}")
print("keys generated successfuly")