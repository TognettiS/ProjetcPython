import smtplib
import email.message

def enviar_email():
    corpo_email = f"""
    <p>Teste Email Automático Python!</p>
    <p>Email recebido com sucesso!!!</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Testando Email"
    msg['From'] = '2503.gui@gmail.com'
    msg['To'] = '2503.gui@gmail.com'
    password = 'xgwyulavosschiqq'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()
