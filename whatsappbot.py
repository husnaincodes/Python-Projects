import pywhatkit
phone_number = (input("Enter the Phone number of receiver in (+92): "))
message = input("Enter the message you want to sent: ")


time = int(input("Enter the time in hours : "))
minutes  = int(input("Enter the number in minutes(1,2,3,10): "))

pywhatkit.sendwhatmsg(phone_number,message,time,minutes)
