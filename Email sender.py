
import smtplib as s

from getpass import getpass 


user = input("Enter Your Email Please: ")

password = getpass("Enter Your password please: ")

email = s.SMTP("smtp.gmail.com",587)

email.ehlo()

email.starttls()

email.login(user,password)

subject =input("Please Enter Your Subject :")

body = input("Enter Your message body please :")

message = "Suject: {}\n\n{}".format(subject,body)

listadd = ["Husnain.tayab@hotmail.com","husnaintayab6@gmail.com"]

email.sendmail(user,listadd,message)

print("SEND EMAIL SUCCESSFULLY!")

email.quit()




