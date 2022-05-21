import smtplib

try:
    smtpObj = smtplib.SMTP("smtp.gmail.com", 587) 
    smtpObj.starttls()
    smtpObj.login("kolya.com145@gmail.com", "Kolya14102005") 
    smtpObj.sendmail("kolya.com145@gmail.com", "kolya.com145@gmail.com", 'msg')
except:
    print('Error with email')
finally:
    smtpObj.quit()
