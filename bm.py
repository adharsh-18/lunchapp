import smtplib
from email.message import EmailMessage
import pandas as pd

data = pd.read_excel("sample.xlsx","data")
# data = pd.read_excel("main.xlsx","data")          uncomment this for sending to delegates
d = data[["ID","MAIL","NAME"]]

def gen_message(name,id):
    message = f"""
<h1>   
Dear {name},
</h1>
<p>
We hope this message finds you well and filled with anticipation for the conference! As the event draws near, we are excited to share some essential information with you.
</p>

<h2>Conference Brochure:</h2>
<p>To ensure your participation in the conference is as seamless as possible, we have attached a link to the SSN-SNUC MUN Conference Brochure. We request you to review the manual thoroughly in preparation for the event. </p>
    <p>https://drive.google.com/file/d/1zqh2lsUgPG62J_W0AqYb_VAHlzmiei4J/view?usp=sharing</p>
<h2>Unique Lunch ID:</h2>
<p>In our commitment to providing you with a pleasant experience during the conference, we are pleased to introduce a new initiative this year. Instead of traditional meal vouchers, we will be issuing a unique Lunch ID to you for your convenience. Reading out this ID to our staff will give you access to your lunch and other refreshments during the 3 days of the conference.
</p>
   <h3> Your Lunch ID is: {id}</h3>
<p>
To ensure a smooth distribution process during the conference, we kindly request you to follow these steps:
</p>
<h2>Star this Email:</h2>
<p>Please mark this email as important to ensure easy access to it during the conference.
</p>
<h2>Lunch Redemption:</h2>
<p>Present your Lunch ID at the designated lunch area during the conference. Our staff will verify the ID and confirm your identity for lunch service.</p>

<p>
Should you have any questions or concerns regarding the conference or any related matters, please do not hesitate to reach out to our organizing team. We are here to assist you and ensure that your participation in SSN-SNUC MUN is both fulfilling and memorable.
</p><p>Thank you for your dedication and enthusiasm for the conference. We eagerly await your presence and look forward to fostering meaningful discussions and collaborative solutions.
</p>
<p>Warm regards,</p>
<p>The Organizing Committee</p>
<p>SSN-SNUC MUN 2024
</p>
"""

    return message


def send_mail(name,id,email):
    msg = EmailMessage()
    msg.set_content(gen_message(name,id),subtype = 'html')
    msg['Subject'] = 'SSN SNUC MUN Conference Details'
    msg['From'] = ""          # from email
    msg['To'] = email
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('email','pass')###email id and create a spl password for 2 step verif
    server.send_message(msg)
    server.quit()

for i in range(len(d)):
    send_mail(d.iat[i,2],d.iat[i,0],d.iat[i,1])
