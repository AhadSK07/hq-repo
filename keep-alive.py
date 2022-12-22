from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror

RENDER_EXTERNAL_URL = environ.get('RENDER_EXTERNAL_URL', '')
if RENDER_EXTERNAL_URL != 0:
    while True:
        try:
            rget(RENDER_EXTERNAL_URL).status_code
            sleep(1200)
        except Exception as e:
            logerror(f"keep-alive.py: {e}")
            sleep(2)
            continue
