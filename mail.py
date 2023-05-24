import smtplib, ssl
import random
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender = "hybmaheshreddy@gmail.com"
password="uunxymdkjcrilijm"
cc="anannyaps001@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = " WISH YOU Happy Birthday Sir -TEST MAIL "
message["From"] = sender
to = sys.argv[1]
name= sys.argv[2] + sys.argv[3]
branch= sys.argv[4]
course= sys.argv[5]
activity= sys.argv[6]
message["to"] = to
to=['vizmahesh18@gmail.com']
message["Cc"] = cc
html = """\
        <html>
          <body>
            <h1> Dear  </h1>
            <h1 style="color:blue;" >Wish""" + name+"""  you happy Birthday On behalf of GSSS(R) </h1><br>
            <h3>  we wish a great day and career ahead at GSSS</h3
      <h2>Missed Class Attendance Form - Details</h2>
      <p><strong>Name:</strong> """+ name + """</p>
      <p><strong>Branch:</strong>"""+ branch+"""</p>
      <p><strong>Course:</strong> """+course+"""</p>
      <p><strong>Activity:</strong>"""+activity+"""</p>
       <p>Please find the document proof attached.</p>
    </body>
    </html>
        
        """
       
part2 = MIMEText(html, "html")
message.attach(part2)
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender, password) #login with mail_id and password
text = message.as_string()
session.sendmail(sender,to, text)

print('email sent successfully')



session.quit()
pass