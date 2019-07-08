import smtplib

MY_PASSWORD = 'contrasenha'
USER = 'usuario@email.com'

try:
    smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print(smtp_obj.ehlo())
    print(smtp_obj.login(USER, MY_PASSWORD))

    smtp_obj.sendmail(USER, 'usuario2@email.com', "Subject: test alpha beta gamma \n Hello this is a test")
except:
    print("Ocurrio un error al enviar el correo.")

print(smtp_obj.quit())
