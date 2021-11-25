import smtplib

sender = "joaopaulo@scobinengenharia.com.br"
receiver = "jpg73@cam.ac.uk"
password = "@Teste2021"
subject = "Teste Python"
body = "This is a test"

#header
message = f"""From: {sender}
to: {receiver}
subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.scobinengenharia.com.br", 587)  #Two arguments
server.starttls()
try:
    server.login(sender, password)  #login
    print("Logged in...")
    server.sendmail(sender, receiver, message)  #send an email.
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in.")
