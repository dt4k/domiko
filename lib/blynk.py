from os import path, environ
import json
import requests

class BlynkClient(object):
    HOST = 'http://blynk-cloud.com'
    HEADERS = {'Content-Type': 'application/json'}

    def __init__(self, token=environ.get('BLYNK_TOKEN')):
        self._token = token

    def _uri(self, *args):
        return path.join(str(self.HOST), str(self._token), *args)

    def get_pin(self, pin):
        res = requests.get(self._uri('get', pin))
        return res.json().pop()

    def is_hardware_connected(self):
        res = requests.get(self._uri('isHardwareConnected'))
        return res.json() #true/false

    def put_pin(self, pin, val):
        data = [val]
        res = requests.put(
            self._uri('update', pin),
            headers=self.HEADERS,
            data=json.dumps(data)
        )
        res.raise_for_status()
        return val
