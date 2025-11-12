
import random
def otp_generator(length = 4):
    if length<0:
        
        raise ValueError("Otp lenght must be postive")
    otp = "".join([str(random.randint(0,9)) for i in range(length)])
    return otp

otp = otp_generator()
print(f"Your otp is : {otp}")