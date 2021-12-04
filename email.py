import imaplib
import email
from email.header import decode_header

class Email:

    def login():
        # account credentials
        username = input("Enter Email Address: ")
        password = input("Enter Password: ")

        # create an IMAP4 class with SSL
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        # authenticate
        imap.login(username, password)

        return 1

    def logout():
        # close the mailbox
        imap.close()
        # logout from the account
        imap.logout()

        return 1

    def enterMailBox():
        # select the mailbox I want to delete in
        # if you want SPAM, use imap.select("SPAM") instead
        imap.select("INBOX")

        return 1

    def filterBySender():
        # search for specific mails by sender
        status, messages = imap.search(None, 'FROM "orders@oe.target.com"')

        return 1

    def filterByKeyWord():
        # to get mails by subject
        status, messages = imap.search(None, 'SUBJECT "Welcome"')

        return 1

    def filterByDate():
        # to get mails after a specific date
        status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
        # to get mails before a specific date
        status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')

        return 1

    def getAllMail():
        # to get all mails
        status, messages = imap.search(None, "ALL")

        return 1

    def getMailIDs():
        # convert messages to a list of email IDs
        messages = messages[0].split(b' ')

        return 1

    def deleteMail():
        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            # you can delete the for loop for performance if you have a long list of emails
            # because it is only for printing the SUBJECT of target email to delete
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if it's a bytes type, decode to str
                        subject = subject.decode()
                    print("Deleting", subject)
            # mark the mail as deleted
            imap.store(mail, "+FLAGS", "\\Deleted")

        return 1

    def emptyBin():
        # permanently remove mails that are marked as deleted
        # from the selected mailbox (in this case, INBOX)
        imap.expunge()
