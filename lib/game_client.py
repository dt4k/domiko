from os import environ
from lib import blynk


class GameClient(object):

    def __init__(self, token=environ.get('BLYNK_TOKEN')):
        self.pins = {
            'timer': 'v0',
            'start': 'v20',
            'pause': 'v12',
            'reset': 'v21',
            'red': {
                'alpha': 'v1',
                'bravo': 'v2',
                'charlie': 'v3',
                'score': 'v7'
            },
            'yellow': {
                'alpha': 'v4',
                'bravo': 'v5',
                'charlie': 'v6',
                'score': 'v10'
            }
        }
        self.blynk = blynk.BlynkClient(token)


    async def timer(self):
        return self.blynk.get_pin(self.pins['timer'])

    async def start(self):
        print('game starting')
        return self.blynk.put_pin(self.pins['start'], '1')
    async def pause(self):
        print('game pause')
        return self.blynk.put_pin(self.pins['pause'], '1')
    async def reset(self):
        print('game reset')
        return self.blynk.put_pin(self.pins['pause'], '1')
    async def red_score(self):
        return self.blynk.get_pin(self.pins['red']['score'])
    async def red_alpha(self):
        return self.blynk.get_pin(self.pins['red']['alpha'])
    async def red_bravo(self):
        return self.blynk.get_pin(self.pins['red']['bravo'])
    async def red_charlie(self):
        return self.blynk.get_pin(self.pins['red']['charlie'])
    async def yellow_score(self):
        return self.blynk.get_pin(self.pins['yellow']['score'])
    async def yellow_alpha(self):
        return self.blynk.get_pin(self.pins['yellow']['alpha'])
    async def yellow_bravo(self):
        return self.blynk.get_pin(self.pins['yellow']['bravo'])
    async def yellow_charlie(self):
        return self.blynk.get_pin(self.pins['yellow']['charlie'])
