import re

text = """
Contact us at student@example.com or admin@college.edu.
You can also email test.email123@gmail.com for more information.
"""

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

emails = re.findall(email_pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)
