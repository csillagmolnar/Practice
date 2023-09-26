import maskpass
import smtplib

from cryptography.fernet import Fernet
from email import encoders
from email.mime import MIMEText
from email.mime import MIMEBase


server = smtplib.SMTP('smtp.gmail.com', 25)

# function to start the process
server.ehlo()

# mask password
password = maskpass.advpass()
email = input('Enter your email address: ')

server.login(email, password)
