## Solve:
- [ ] Unarchive recursively a zip containing directories with files: one of them has the flag 
  <br>
  ```bash
  unzip linux-1.zip -d temp
  for i in `ls temp`; do unzip temp/$i -d temp ;done
  { grep -Ri flag temp | cut -d":" -f 2 | sort -u } 2>/dev/null
  ```

<br>

## Flag:
`flag{you_found_me}`
