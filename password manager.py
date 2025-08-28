from cryptography.fernet import Fernet
# def write_key():
#     key = Fernet.generate_key
#     with open("key.key",'wb')as key_file:
#         key_file.write(key)
# def load_key():
#     file = open("key.key","rb")
#     key= file.read()
#     file.close()
#     return key
# key = load_key()
# fer = Fernet(key)
def view():
    with open("password.txt",'r') as f :
        for line in f.readlines():
            data = line.strip()
            user, password = data.split("|")
            print(f"User: {user}   Passwrod: {password}")
            # fer.decrypt(password.encode().decode())
        
def add():
    name = input("Enter your account name: ")
    pwd = input("Enter your password: ")
    with open("password.txt",'a') as f :
        f.write(f"{name}|{pwd} \n")
while True:
    mode = input("Would you like to add new password or view the existing one (add , view)? .Press q for quit: ")
    if mode == "q":
        break
    elif(mode=="view"):
       view()
    elif(mode=="add"):
        add()
    else:
        print("Invalid key!")
