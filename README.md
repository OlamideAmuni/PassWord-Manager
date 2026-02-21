# PASSWORD MANAGER

## Description
A simple terminal based tool that securely store passwords,it is built with python amd it uses cryptography (fernet) library  to safely encrypt and decrypt passwords.

## FEATURES
- Adds new password
- encrypts the new password and save it
- decrypts saved password for viewing
- stores each saved password in a text file.
- 
## TOOLS AND TECH USED
- Python 3.10+
- cryptography(fernet) library
- Visual Studio Code
- 
## STEP BY STEP ON HOW I BUILT PASSWORD MANAGER 
- I created a folder for my project, the folders contains all file i need for the password manager
- I generated fernet key using cryptography, which is a python library.this program generate the key for encryption and decryption
  
  -[Generated key code](generate_key.py)
- created my main program file named password_manager.py. in this file
   - i loaded the key i generated
   - Created Menu options
   - define function for each menu option
   - Used While loop to loop through menu options
   - Also created file for storing passwords
     
     -[password manager code](password_manager.py)

## IDEA BEHIND PROJECT
Let say this is Terminal-Based-Password-MAnager built with python using cryptography library.
Passwords can easily and be stored securely using this tool. it can store and manage different or multiple account securely beacuse it is saved in an encrypted form,reducing the risk of passwords exposure.

In cybersecurity, CIA triad is a key aspect every action must follow
- Confidentiality: this means keeping data safe, with this password manager, i make sure password are in encryption mode and not accessible to the public.

- Integrity: i kept the saved pasword accurate in a normalized format, so tampering with it cam easily be detected

- Availability: this tool is available only to authorized user, right now this is available to everyone, and will work on keeping it to only authorized use by adding authentication to it. 



 

  
