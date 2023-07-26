import smtplib
from email.message import EmailMessage

# I WILL BE USING SMTPLIB AND SEND TO EMAIL BECAUSE TWILIO CANNOT WORK :(
class NotificationManager:

    def __init__(self):
        self.myemail = "rizkymaulanahadi27@gmail.com"
        self.password = "YOUR EMAIL API KEY"

    def send_message(self, send_to: list, contents: list):
        #Solution found in stackoverflow, conventional ways of sending email (using sendmail()) would not display subject of utf-8 encoded text. https://stackoverflow.com/questions/5910104/how-to-send-utf-8-e-mail/71901202#71901202
        connector = smtplib.SMTP("smtp.gmail.com") #Create the object specifying our email provider's smtp link(?). Which for google is smtp.gmail.com
        connector.starttls()
        connector.login(user=self.myemail, password=self.password)
        for content in contents:
            for user in send_to:
                msg = EmailMessage()
                content['content'] = f"Hi {user['firstName']} {user['lastName']}!\n{content['content']}"
                msg.set_content(content["content"])
                msg['Subject'] = content["subject"]
                msg['From'] = self.myemail
                msg['To'] = user['email']
                connector.send_message(msg)
            
        connector.close()