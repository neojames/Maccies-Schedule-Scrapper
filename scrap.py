#!/usr/bin/python

# Scrap.py
# Main program logic; Scraps scheduling data from peoplestuffuk.com, checks to see if it has been updated, and if it has
# updates a shared calender. Program logic file.
# Published under the Apache License 2.0, maintained by James Bolton (james@neojames.me)

# TODO: Write program logic, tieing together sub-programs and preforming comparrisons.

import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from config import *

password = password.encode()
salt = salt.encode()
passkey = passkey.encode()

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(passkey))
key = Fernet(key)
password = key.decrypt(password)
password = password.decode()

os.system('python logic/scrapper.py ' + username + ' ' + password)
