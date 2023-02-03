## Solve:

- [ ] Extract only the last octet
  ```bash
  cat IPs | rev | tac | cut -d"." -f1 | tr "\n" " "
  ```

<br/>

- [ ] Hex encoded values form the flag
  `72 65 67 65 78 67 75 79 68 65 72 65`
  
<br/><br/>

## Flag:
`flag{regexguyhere}`
