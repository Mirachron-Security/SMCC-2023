## Intro:

I intercepted the traffic between this pentester and his victim. 
Can you help me find the answers to the next questions?

To check your answers, run the script and if you get it right, you will get 
the corresponding letter for the final flag.

**For example**: If you find that the answer to question 1 is "http://google.com", then you will execute:
> `python3 verify.py 1 "http://google.com"`

Flag format: `flag{combined_characters}`

<br/>

### Questions:
<br/>

1. What is the URI the attacker accessed in order to login to the webpage?
2. What CMS was the page using?
3. What are the credentials that logged the attacker on the webpage? 
*(How can you tell you found the right credentials)* <br/>
**Format: `user:password`** 
4. What is the URL that showed the attacker a number of possible usernames? 
5. What file did the pentester actually retrieve from the machine to list the users?
6. The attacker also downloaded a file from the server. What is it named?
7. This downloaded file hides a message. Can you figure out what it is?
8. What is the first disallowed entry that is displayed by the web server?
9. Who else is allowed to visit the web server on the other accessible port?
10. What are the credentials for the FTP server? <br/>
  **Format: `user:password`**
11. What is the name of the folder that hides a ZIP archive?
12. What kind of web attack was performed against the login form?
13. The attacker tried a web attack but didn't succeed. What was it and what is the resource he was trying to retrieve? 
**Format: `attack:file`** (use abbreaviated name of the attacka)
14. List all the available ports that the victim machine is listening on separated by commas, in ascending order.

<br/>

Hints are allocated in order for questions 3,7,10.

<br/><br/>

## Files:

[sniff away 1400.zip](https://github.com/ChronosPK/Sibiu_Academic_CTF/files/10310688/sniff.away.1400.zip)
