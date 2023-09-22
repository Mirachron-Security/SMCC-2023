## Solve:
- [ ] add the user
  ```bash
  sudo useradd CTF
  sudo usermod -u 2023 -g 1000 CTF
  ```

- [ ] check linux file
  ```bash
  cat /etc/passwd | tail -n1
  ```

<br>

## Flag:
**`flag{CTF:x:2023:1000::/home/CTF:/bin/sh}`**
