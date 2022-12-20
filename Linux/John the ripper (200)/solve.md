## Solve:

- [ ] Crack the zip password 
  ```bash
  zip2john zipfile.zip > hash.txt
  john --format=zip hash.txt
  ```

- [ ] Cracking linux password hashes
  ```bash
  unshadow passwd shadow > unshadowed
  john --wordlists=/usr/share/wordlists/rockyou.txt unshadowed
  ```

<br/>

## Flag:
`flag{iloveyou20}`
