## Download a blank website and introduce the flag in a rondom location (js file)

```bash
git clone https://github.com/cloudacademy/static-website-example.git
cat static-website-example/assets/js/jquery.min.js | sed "s/ra.thead,ra.th=ra.td;/&ra.thead,ra.th=ra.td;flag{grep_w1ll_d0_7h3_j0b}/g" > temp
mv temp static-website-example/assets/js/jquery.min.js 
```
