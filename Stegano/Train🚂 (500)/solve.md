## Solve:
1. list files of archive (password protected)
```bash
unzip -l archive.zip
```
All files start with "`796F75`" one file is called "`images-10/X2FuZF9tZQo=`"
<br/><br/><br/>

2. decode the name of most popular files from hex (`796F75`) and the second from base64 (`X2FuZF9tZQo=`) and you get "`you_and_me`", which is the archive password
```bash
unzip -P 'you_and_me' archive.zip
```
<br/><br/>

3. scan QR codes and extract a letter from each. In order, will construct the final flag.
```bash
for i in {1..50}; do zbarimg images-$i/* > out-$i; done
for i in {1..50}; do cat out-$i| cut -d "." -f3 | tr -d "\n"; echo ; done | sort -u
```
<br/><br/>

## Flag:
`flag{awesome_thing_you_did}`
