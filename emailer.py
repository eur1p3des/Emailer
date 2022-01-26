import smtplib
import ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from getpass import getpass


# Define basic attributes
from_addr = input("Please enter your email address: ")
password = getpass("Please enter your account password: ")
to_addr = input("Please enter the receiver address: ")
subject = input("Please enter the subject: ")

# Creating the content for the message
print("Please enter the content of the message (ended with EOF): ")
lines = []
line = input()
while line != 'EOF':
    lines.append(line)
    line = input()
content = '\n'.join(lines)

# Asking for the attachment name
filename = input("Please input the full path of the file you want to send: ")

# Defining the mail server and the port
server1 = 'smtp.gmail.com'
port1 = '465'
server2 = 'smtp-mail.outlook.com'
port2 = '587'
print("Please choose one of the following servers:")
print("[1] Gmail")
print("[2] Outlook (hotmail account)")
option = int(input("Choose your server (number): "))
if option == 1:
    server = server1
    port = port1
    print('You have chosen ', server, ' that operates on the port: ', port)
else:
    server = server2
    port = port2
    print('You have chosen ', server, ' that operates on the port: ', port)



# Build the message object
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

# Attach the desired file
with open(filename, 'rb') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)


#Create a context for the ssl connection
context = ssl.create_default_context()


#Send mail
print('Sending mail')
server = smtplib.SMTP_SSL(server, port, context=context)
server.login(from_addr, password)
server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])
print('Succeeded to send mail')
