from cryptography.fernet import Fernet


def load_key():
    with open("password_key" , "rb") as read_key: #this opens password_keys file and read binary "rb", meaning read it content
        return read_key.read()  #returns the content we read in read_keys so we can use
    
key = load_key() # secret code that helps lock and unlock passwords 
fer = Fernet(key) #we are using "fer" to create an object to decrypt and encrypt password using "key"

def main_menu():

    print("*"*20)
    print("PASSWORD MANAGER")
    print("*"*20)
    print("1. Add Password\n")
    print("2. View Password\n")
    print("3. Exit Password Manager\n")



def ADD_password():
    print("\n-------Adding Passwords-------")
    name = input("Account Username \n")
    password = input("Add Your Acoount Password: \n")
    
    with open("passwords.txt" , "a") as acct_pass:
        acct_pass.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

    print(f"Password for Account Name {name} is saved")

def View_password():
    print("--------Saved Passwords-------\n")
    try:  # "try" help opens password.txt.
        with open("passwords.txt" , "r") as file:
            for lines in file.readlines():
                data = lines.rstrip() # "rstrip" help remove any unwanted characters like space at the right end of each line
                name, encrypted_pwd = data.split("|") #split removes the seperator "|" in content in data and turne the rsult into a list
                print(f"account: {name} | password: {fer.decrypt(encrypted_pwd.encode()).decode()} \n") 
    except: # if "try" does not open password.txt probably because the file is not found, then there is no saved password
        print("No saved Password Available \n")


while True:
    main_menu()

    User_choice = (input("Enter Choice From Main Menu: \n" ))

    if User_choice == "1":
        ADD_password()
    elif User_choice == "2":
        View_password()
    elif User_choice == "3":
        print("\n You Exited Password Manager, Thank You\n")
        break    
    else:
        print("\n Please Enter a Valid Choice from Main Menu, Thank You\n")
        
            




