## Solve:

- [ ] Analyze the packet capture 
  filter eapol protocol to see the WPA2 handshake intercepted 

- [ ] Crack the WPA2 password from the intercepted handshake
  ```bash
  aircrack-ng crack-it-open.cap -w /usr/share/wordlists/rockyou.txt
  ```

<br/>

## Flag:
`flag{hatehackers}`
