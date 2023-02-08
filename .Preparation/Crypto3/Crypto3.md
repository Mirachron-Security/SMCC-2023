## Intro:

Calculate the SHA256 hash of the given file. <br>
Now, open the file change the amount from 1000 to 9000. <br>
<br>
Calculate the `xor` between the 2 hashes and put the value between `flag{` `}`.
<br>
<br>
You now know an application of `hash`ing : checking the integrity of files. 

<br><br>

## Files:
[order.zip](https://github.com/ChronosPK/Sibiu-Military-Cyber-Challenge/files/10683434/order.zip)

<br><br>

## Solve:

```bash
# calculate the original checksum
sha256sum order.json 
2c34b68669427d15f76a1c06ab941e3e6038dacdfb9209455c87519a3ef2c660  order.json

# modify the "amount" from 1000 to 9000
cat order.json 
{
  "sender": "Alice",
  "recipient": "Mallory",
  "currency": "USD",
  "amount": 9000,
  "notes": "weekly payment"
}

# check the new checksum
sha256sum order.json
11faeec5edc2a2bad82ab116bbe4df0f4bc6edd96adac7150bb4e6364a238466  order.json
```

Now calculate the xor of the 2 hex strings (hashes) [online](https://xor.pw/)

<br><br>

## Flag:
`flag{3dce58438480dfaf2f40ad101070c1312bfe37149148ce505733b7ac74d14206}`
