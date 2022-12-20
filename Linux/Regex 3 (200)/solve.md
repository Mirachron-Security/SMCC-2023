## Solve:

```bash
cat /usr/share/wordlists/rockyou.txt | grep -E  "[a-z].*[A-Z]|[A-Z].*[a-z]" \
| grep -E "[0-9]" | grep -v "^[a-zA-Z0-9 ]*$" | head -n 100 | tail -n 1
```

<br/>

## Flag:
`flag{M&M4ever}`
