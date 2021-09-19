import smtplib
import email.message
from password import password_email

def send_message(token, ameil):
    corpo_email = f"""
    <h1>Teste</h1>
    <p>Terceiro teste teste de disparo de email</p>
    <p>http://0.0.0.0:8000/signup?token={token}</p>
    <p>att Helder</p>
    """

    msg = email.message.Message()
    msg['subject'] = "Primeito teste de disparo de email"
    # msg['From'] = "querybusines31@gmail.com"
    msg['From'] = "heldermenegatti720@gmail.com"
    msg['To'] = f"{ameil}"
    password = password_email() #  senha do email from
    msg.add_header('content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("Email enviado") 