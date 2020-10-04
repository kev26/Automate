import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(((\d\d\d)|(\(\d\d\d\)))?            # area code (optional)
(\s|-)            # first separator
\d\d\d            # first 3 digits
-            # separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)
(\d{2,5}))?)           # extension (optional)

''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5})?.com
[a-zA-Z0-9_.+]+            # name part
@                          # @ symbol
[a-zA-Z0-9_.+]+            # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allphonenumber = []
for phonenumber in extractedPhone:
    allphonenumber.append(phonenumber[0])

print(allphonenumber)
print(extractedEmail)
# Copy the extract email/phone to the clipboard
results = '\n'.join(allphonenumber) + '\n' + '\n'.join(extractedEmail) + '\n'
pyperclip.copy(results)