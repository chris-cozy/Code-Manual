# Import library
# SMTP() - Create smtp object for server
    # smtp protocol, port number
    # Use 587 or 465
        # By using 587, you are using TLS encryption
        # If they don't work, try not passing in no port number
# ehlo() - Greet server and establish connection
# starttls() - Start encryption
# Enter username and password
    # Using the input function will prevent people from knowing your password if they see the script
    # You can also use the getpass library to hide your password while typing
# login() - Login using username and password
import smtplib
import getpass

from matplotlib.pyplot import getp
smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
smtp_object.starttls()

password = getpass.getpass("Enter password: ")
email = getpass.getpass("Email: ")

smtp_object.login(email, password)

# Now we are logged in
# from_address - Your email
# to_address - Email you are sending to
# The funcion to send the email takes in one long string in a specific format
    # Use variables for the subject and message text
# sendmail() - Sends the email
    # If an empty dictionary is returned that means the email was sent successfully
# quit() - Quit and close the session
from_address = email
to_address = "example@example.com"
subject = input("Enter the subject line: ")
message = input("Enter the body message: ")
msg = "Subject: " + subject + "\n" + message

smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()



