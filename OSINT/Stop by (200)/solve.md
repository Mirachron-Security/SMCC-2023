## Solve:

- Challenge description points us to gas prices
- We also see at the bottom of the photo some strange shape as a tripod, and image seems distorted as in fish lens or 360 view.

<br/>

Get the conclusion that we must get to that location using google maps, <br/>
Look around for the closest gas station (right behind), <br/>
And try to `extract` the flag. For that, we will use `steghide`.

<br/>

```bash
steghide extract -sf photo\ of\ military\ school.jpg
Enter passphrase: 6.97
wrote extracted data to "flag.txt".
```

<br/><br/>

## Flag:

`flag{i_was_the_guy_with_the_camera_for_google}`
