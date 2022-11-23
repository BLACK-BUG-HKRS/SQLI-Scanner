# SQLI-Scanner
SQL Injection Scanner

To run this:

- `pip3 install -r requirements.txt`

Provide URL in the command Line argument

```
python sqliscanner.py http://testphp.vulnweb.com/artists.php?artist=1
```

Output:

```
[!] Trying http://testphp.vulnweb.com/artists.php?artist=1"
[+] SQL Injection vulnerability detected, link: http://testphp.vulnweb.com/artists.php?artist=1".
```
