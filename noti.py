class Noti:
    def send(self,message):
        print("Sending Notifiation.....")

class email(Noti):
    def send(self, message):
        print(f"Sending Email: {message}")
class sms(Noti):
    def send(self,message):
        print(f"Sending SMS: {message}")
class telegram(Noti):
    def send(self, message):
        print(f"Sending Telegram: {message}")
class viber(Noti):
    def send(self, message):
        print(f"Sending Viber: {message}")

class noti_context:
    def __init__(self,strategy):
        self.strategy=strategy
    def execute_noti(self,message):
        self.strategy.send(message)
        
Email=email()
SMS=sms()
Tele=telegram()
Viber=viber()

noti=noti_context(Email)
noti.execute_noti("Hello! Nice to meet you..")
noti=noti_context(SMS)
noti.execute_noti("Your exam is tomorrow!!!")
noti=noti_context(Tele)
noti.execute_noti("Goodluck..Honey!!")
noti=noti_context(Viber)
noti.execute_noti("I Love You,Baby!!")