## Intro:

I intercepted the traffic between this pentester and his victim. 
Can you help me find the answers to the next questions?

To check your answers, make a POST request to **`http://213.177.18.70:31337/sniff_away/<question>`**, where `<question>` is a number from 1 to 14 for each question.  

**For example**: If you find that the answer to question 1 is "http://google.com", then you will make the following reuqest:
> `curl -X POST -d 'http://google.com' http://213.177.18.70:31337/sniff_away/1`

Flag format: `flag{combined_characters}`

<br>

### Questions:
<br>

1. What is the URL the attacker accessed in order to login to the webpage?  <br>
**Format: `http://IP/location/filename`** 
2. What CMS was the page using?
3. What are the credentials that logged the attacker on the webpage? <br>
**Format: `user:password`** 
4. What is the URL that showed the attacker what users are on the machine?  <br>
**Format: `http://IP/location/filename`** 
5. What is the name of the system file that the pentester actually retrieve from the machine to list the users?
<br>
**Format: `/path/to/file/on/the/machine** 
6. The attacker also downloaded a file from the server. What is it called?
7. This downloaded file hides a message. Can you figure out what it is?
8. What is the first disallowed entry that is displayed by the web server?
	9. Who else is allowed to visit the web server on the other accessible port?
10. What are the credentials for the FTP server? <br>
  **Format: `user:password`**
11. What is the name of the folder that hides a ZIP archive? (you can find the answer in the FTP communication)
12. What kind of web attack was performed against the login form?
13. The attacker tried a web attack but didn't succeed. What was it and what is the resource he was trying to retrieve? 
**Format: `attack:/path/to/localfile`** (use abbreaviated name of the attack)
14. List all the available ports that the victim machine is listening on separated by commas, in ascending order.

<br>

Hints are allocated in order for questions 3,7,10.



<br><br>

## Files:

[sniff-away.zip](https://github.com/ChronosPK/Sibiu-Military-Cyber-Challenge/files/10697784/sniff-away.zip)

