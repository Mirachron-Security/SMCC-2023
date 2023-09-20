## Create:

1. First:
```bash
openssl aes-256-cbc -pbkdf2 -iter 10000 -e -in first.txt -out first.txt.openssl     

# enter AES-256-CBC encryption password: password123
# Verifying - enter AES-256-CBC encryption password: password12
```

2. Second:
```bash
gpg --symmetric --cipher-algo aes256 second.txt

# Password: password123
```
