import EmailFunctions as Email

e = Email.Email()

# log in
print("logging in ...")
e.login()
print("logged in !")

# Enter inbox
print("entering INBOX ...")
e.enterMailBox()
print("entered INBOX !")

# find emails sent by target
print("Finding Emails from 'orders@oe.target.com' ...")
e.filterBySender()

e.getMailIDs()

print("Found Emails at:")
e.viewMail()

# find emails with keyword in subject: Welcome
print("Finding Emails with 'Welcom' in Subject ...")
e.filterByKeyWord()

e.getMailIDs()

print("Found Emails at:")
e.viewMail()

# log out
print("logging out ...")
if (e.logout()):
    print("logged out !")
else:
    print("did not log out")
