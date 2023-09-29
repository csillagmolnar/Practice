import hashlib
import sys

# Handle requests is installed
try:
    import requests
except ImportError:
    print('Install requests package')
    exit()

def lookup_password(password):
    pwd_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    pwd_hash_head = pwd_hash[:5]
    pwd_hash_tail = pwd_hash[5:]
    URL = 'https://api.pwnedpasswords.com/range/' + pwd_hash_head
    
    try:
        res = requests.get(URL)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    res_result = (line.split(':') for line in res.text.splitlines())

    count = next(count for hash_tail, count in res_result if hash_tail == pwd_hash_tail)

    return pwd_hash, count