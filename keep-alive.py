from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror

BASE_URL = environ.get('BASE_URL')
if BASE_URL:
    while True:
        try:
            rget(BASE_URL).status_code
            sleep(1200)
        except Exception as e:
            logerror(f"keep-alive.py: {e}")
            sleep(2)
            continue
