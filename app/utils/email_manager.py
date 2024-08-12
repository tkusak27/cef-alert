import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.helpers import get_env_var

def get_subject():
    subject = '''
    '''
    return subject

def get_body():
    body = '''

    '''
    return body
    
def send_email():
    sender_email = get_env_var("sender_email")
    receiver_email = get_env_var("receiver_email")
    subject = 'Fund Updates'
    body = get_body()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(sender_email, get_env_var("email_key"))

        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()