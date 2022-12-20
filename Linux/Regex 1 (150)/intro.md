## Intro:

How many passwords in rockyou.txt start and end in numbers? <br/>
Flag format: flag{number}
<br/>
You can use `grep` and `wc`.

<br/> 

## Further info:
`[]`	Character Set: matches any single character/range of characters inside
<br/>
`.`	Wildcard: matches any character
<br/>
`*`	Star / Asterisk Quantifier: matches the preceding token zero or more times
<br/>
`+`	Plus Quantifier: matches the preceding token one or more times
<br/>
`{min,max}`	Curly Brace Quantifier: specifies how many times the preceding token can be repeated
<br/>
`()`	Grouping: groups a specific part of the regex for better management
<br/>
`\`	Escape: escapes the regex operator so it can be matched
<br/>
`?`	Optional: specifies that the preceding token is optional
<br/>
`^`	Anchor Beginning: specifies that the consequent token is at the beginning of the string
<br/>
`$`	Anchor Ending: specifies that the preceding token is at the end of the string
