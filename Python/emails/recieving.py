# Checking your inbox in python
# IMAP4_SSL() - Creating an IMAP object. Enter the email server
# Store your email and app-password
# .login(email, pass) - login to your email account
# .list() - list all email folders that you are able to check
# .select() - Enter an email folder name to select
    # Returns a confirmation and connection number to the inbox
import imaplib
import getpass
import email
M = imaplib.IMAP4_SSL("imap.gmail.com")
email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")

M.login(email, password)
M.list()
M.select("inbox")

# Once you are in the desired email folder, you can now use the special syntax to search through it
# .search(None, "") - Search through the inbox. First argument will be None, second will be the special syntax
    # Returns a tuple, so use tuple unpacking
    # type - confirmation
    # data - email id. If there is a list of multiple ids, that means multiple emails fit the search criteria
# .fetch(email id, protocol) - Fetches the desired email
    # protocol = "(RFC822)"
    # Returns a tuple, so use tuple unpacking
    # email_data - all the email's data, including the subject and message
# Example - searching for emails with the subject line "IMPORTANT"
type, data = M.search(None, 'SUBJECT "IMPORTANT"')

email_id = data[0]
result, email_data = M.fetch(email_id, "(RFC822)")
raw_email = email_data[0][1]

# Decoding the email string
# Now that we have the email string from the data, it needs to be decoded
# Use the email library
# .decode() - decode the email in case of special characters
# .message_from_string() - Convert the string into an email message
    # Returns an iterator
# Traverse through each part of the email message, and if the part is plain text, grab the payload and print it.
# If a link is expected to be in the email, use 'text/html'
raw_string = raw_email.decode("utf-8")
email_message = email.message_from_string(raw_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)