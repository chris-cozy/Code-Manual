# Emails
It is possible to send emails, as well as check your inbox for incoming messages in Python. The process is reliant on the admin priviledges on your computer, your network, and your email.
If you are using your work equipment and priviledges are an issue, contact your IT department.
## Emails in Python
To send emails in Python, there are a few steps required.
- Connecting to an email server
- Confirming connection
- Setting a protocol
- Logging on
- Sending the message
### Neccesary Library
There is a built-in library for this: *smtplib*
- This is used for sending emails. Each major email provider has their own SMTP (Simple Mail Transfer Protocol) Server.
For checking inbox, he built-in library: *imaplib*
- This has special syntax for searching through the inbox. This syntax can be found online.
For checking inbox, he built-in library: *email*
### Tutorial/Example
I will be using the Gmail SMTP in this example.
For gmail users, you will need to generate an app password instead of the normal password. This let's gmail know that the python script attempting to access the account is authorized to do so.

For Gmail Users, you need to generate an app password instead of your normal email password. This also requires enabling 2-step authentication. Follow the instructions here to set-up 2-Step Factor Authentication as well as App Password Generation:https://support.google.com/accounts/answer/185833?hl=en/. Set-up 2 Factor Authentication, then create the App Password, choose Mail as the App and give it any name you want. This will output a 16 letter password for you. Pass in this password as your login password for the smtp.
