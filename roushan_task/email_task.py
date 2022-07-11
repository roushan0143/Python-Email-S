import config
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from socket import gaierror
from email.mime.text import MIMEText

class SendEmail:
    start_time = datetime.now()
    mail_sent_day = start_time.strftime("%Y-%m-%d")

    def triggerEmail(self,mailBody, emails, subject):
            port = config.port
            smtp_server = config.smtp_server
            login = config.login
            password = config.password
            sender_email = config.sender_email        
            emails.extend(["xyz@gmail.com","abc@gmail.com"])
            receiver_email = ",".join(emails)
            sender_email = config.sender_email
            message = MIMEMultipart("alternative")
            message["Subject"] = str(subject)
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Cc"] = config.mail_cc
            html= """\
                <html>
                <body>
                <h2 style='text-align:center'>DigiLocker NAD Email Task (Testing)</h2>
                </body>
                </html>
                """+mailBody+"""<br/><br/>Thank You</p>"""
            email_body = MIMEText(html, "html")
            message.attach(email_body)
            smtp_server.starttls()

            try:   
                #print(smtp_server,port)
                for mail_id in emails:
                    #print(smtp_server.noop())
                    smtp_server.login(login, password)

                    smtp_server.sendmail(
                        sender_email, mail_id, message.as_string()
                    )  
            except (gaierror, ConnectionRefusedError) :
                return [False, 'Failed to connect to the server. Bad connection settings?', 'E1010']
            except smtplib.SMTPServerDisconnected as smpt_server_error :
                return [False, smpt_server_error, 'E1011']
            except smtplib.SMTPException as smtp_err :
                return [False, smtp_err, 'E1012']

sendMail = SendEmail()
subject = 'This is a test mail for Task'
emails = []
mailbody = 'This is a sampe mail body'
sendMail.triggerEmail(mailBody = mailbody, emails = emails, subject = subject)