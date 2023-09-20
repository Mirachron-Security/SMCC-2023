## Solve:

### Method 1 - check aliases
- [ ] Many relevant commands have been modified through **aliases** <br>
  We then need to restore the commands we want to use
  ```bash
  unalias cat 
  ```

### Method 2 - alter commands
- [ ] Just like in command injection, change the form of the commands
  ```bash
  l\s .
  l$@s /
  $(tr "[A-Z]" "[a-z]"<<<"LS") /home/user
  c''at /home/user/flag.txt
  ```

<br>

## Flag:
`flag{who_let_the_cat_out?}`
