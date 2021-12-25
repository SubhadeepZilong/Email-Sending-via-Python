# ---------- Packages -----------


import smtplib


# ---------- Information -----------


smail = input("Enter Sender's Email: ")
pwd = input("Enter Password: ")
rmail = input("Enter Reciever's Email: ")
subj = input("Enter your Subject: ")
body = input("Enter your Message: ")
msg = f'Subject: {subj}\n\n{body}'


# ---------- Execution -----------


server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login(smail,pwd)
server.sendmail(smail,rmail,msg)
server.quit()
