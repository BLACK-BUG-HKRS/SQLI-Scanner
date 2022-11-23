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
[!] Trying http://testphp.vulnweb.com/login.php"
[!] Trying http://testphp.vulnweb.com/login.php'
[+] Detected 2 forms on http://testphp.vulnweb.com/login.php.
```
