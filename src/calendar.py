import requests

from config import SCRIPT_URL


class CalendarIO:

    def __init__(self):
        pass

    def insert(self, payload):
        req = requests.get(SCRIPT_URL.format(payload.get('startDate'),
                                             payload.get('endDate'),
                                             payload.get('title'),
                                             payload.get('guests')))
        return
