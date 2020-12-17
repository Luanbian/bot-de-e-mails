import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
email = 'emaildequemenvia@gmail.com'
password = 'senha_do_email'

send_to_email = 'emaildequemrecebe@gmail.com'

subject = 'assunto do e-mail'
message = '''conteudo do e-mail'''

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
input("E-mail enviado com sucesso!")
