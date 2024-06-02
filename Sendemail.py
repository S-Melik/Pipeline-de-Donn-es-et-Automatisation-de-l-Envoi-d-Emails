import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

# Email details
sender_email = "example@gmail.com"
receiver_email = "example@gmail.com"
subject = "Instances ABC"
body_text = "Bonjour, les instances :"
xlsx_file_path = r"C:\Users\user\Desktop\Projects\Project 2\results.xlsx"


# Gmail SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = sender_email
smtp_password = "pamy esko skel kdsb"  # Use an app-specific password if you have 2FA enabled

# Read the Excel file
df = pd.read_excel(xlsx_file_path)

# Convert DataFrame to HTML table
html_table = df.to_html(index=False)

# Create the email
message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Plain text and HTML parts
text_part = MIMEText(body_text, "plain")
html_part = MIMEText(f"<html><body><p>{body_text}</p>{html_table}</body></html>", "html")

# Attach parts to the email
message.attach(text_part)
message.attach(html_part)

# Attach the Excel file
with open(xlsx_file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= results.xlsx",
    )
    message.attach(part)

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Error sending email: {e}")
