# Part 0 - Accessing Gmail Account and Filtering Emails
- A user logs in to their Gmail through our application.
- The user can use filters to find emails in their inbox.
    - They select a date. All emails from before a certain date are gathered.
    - Emails with *Unimportant* specified key words or *Unimportant* specified senders can be gathered.
    - Emails with *Important* specified keywords or *Important* senders can be gathered.
    - Emails with overlap between *Important* specified key words / *Important* senders and *Unimportant* key words / *Unimportant* senders can be gathered.

# Part 1 - Deleting Unwanted Emails
- Adding on to Part 0, emails filtered with *Unimportant* specified key words or *Unimportant* senders will be gathered and then deleted.
- Emails with *Important* specified key words or *Important* senders will **never** be deleted, even if they overlap with *Unimportant* key words or *Unimportant* senders.
    - Emails that have over lap between *Important* and *Unimportant* will be presented to the user for them to decided what should not be deleted and what should be deleted.
- There is an option for the user to clear their Email trashcan, permanently deleting all emails in the trashcan.

# Part 2 - Identifying Top Senders
- When the user uses filters to delete emails, the top *X* senders are identified in a list for the user. (Where *X* is a number specified by user)
- There is an option to analyze Emails in the inboxes (without deleting) to identify top *X* senders. (Where *X* is a number specified by user)

# Part 3 - Gathering Unsubscribe Links for Top Senders
- When the top *X* senders are identified, the "unsubscribe" links are gathered and presented to the user, so they can unsubscribe with ease.


