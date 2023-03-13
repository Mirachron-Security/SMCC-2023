### Create a file which hides the flag:
```plain
What is DMARC and why do you need it?
DMARC stands for Domain-based Message Authentication, Reporting, and Conformance. Simply put, it is a way to authenticate your outgoing email messages. It’s implemented via a DNS record that specifies the desired policy.
Given that most cyberattacks start with a phishing campaign, DMARC security is an important factor. If improperly configured, it can create a lot of damage.
DMARC allows organizations to protect their brand and reputation by preventing attackers from using their domain and subdomains names to conduct phishing attacks. (By the way the flag is flag{ascii_juggling})This can help users from falling victim to such attacks, and also keep the organization from being associated with fraudulent activity.
Email senders are verified using policies. DMARC tells receiving mail servers what to do when they get a message that appears to be from your organization but doesn't pass authentication checks.
DMARC is built on key authentication standards SPF (Sender Policy Framework) and DKIM (Domain Keys Identified Mail). It supplements SMTP, the basic protocol used to send emails because SMTP does not include any mechanisms for implementing or defining policies for email authentication.
SMTP (Simple Mail Transfer Protocol) started back in 1980 and, since then, it has been the go-to protocol when it comes to sending emails. Because it was not created with safety in mind, SMTP does not include any security mechanisms. That's why specialists had to create email security protocols like DMARC to help prevent spoofing and fraud.
```

<br>

### Create a script to encode every character in ASCII:

```python
#!/usr/bin/python3

h = open("text.txt","r")
c = h.read()
h.close()

with open("encoded.txt","w") as f:
	for word in c:
		f.write(str(ord(word)))
		f.write(" ")
```


### Create a script to decode the result (what the player needs):

```python
#!/usr/bin/python3

import re

h = open("encoded.txt")
c = h.read()
h.close()

decoded = ''.join([chr(int(dec)) for dec in c.split()])

# select only the portion including the flag
print(''.join(re.findall('flag{.*}',decoded)))
```


### Get the flag:
```bash
python3 decode.py
flag{ascii_juggling}
```
