
email = input("Enter Your Email :")
k= 0
j = 0
d = 0
if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            if(email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1
                if k==1 or j==1 or d ==1:
                    print("Worng Email!")
                else:
                    print("Email is Valid!")
            else:
                print("CORRECT THE DOT POSITION/ Complete the .com")

        else:
           print ("This @ sign place at wrong position")
    else:
        print("First letter should be Alhphabet")

else:
    print("EMAIL LENGTH INVALID!")
