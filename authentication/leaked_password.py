import hashlib
import sys

from typing import Tuple

# Handle requests is installed
try:
    import requests
except ImportError:
    print('Install requests package')
    exit()


def lookup_password(password: str) -> Tuple[str, str]:
    pwd_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    pwd_hash_head = pwd_hash[:5]
    pwd_hash_tail = pwd_hash[5:]
    URL = f'https://api.pwnedpasswords.com/range/{pwd_hash_head}'

    try:
        res = requests.get(URL)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    res_result = (line.split(':') for line in res.text.splitlines())

    count = next(count for hash_tail, count in res_result if hash_tail == pwd_hash_tail)

    return pwd_hash, count


def main(arg):
    correct_form_pwd = arg.strip()
    pwd_hash, count = lookup_password(correct_form_pwd)
    print(f"""
          Your password: {correct_form_pwd}
          Hash of your password: {pwd_hash}
          Number of your password is leaked: {count} """)


if __name__ == '__main__':
    main(sys.argv[1])
