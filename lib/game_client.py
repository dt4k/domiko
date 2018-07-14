import blynk


class GameClient(object):

    def __init__(self, token):
        self.pins = {
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

    def start(self):
        return self.blynk.put_pin(self.pins['start'], '1')

    def pause(self):
        return self.blynk.put_pin(self.pins['pause'], '1')

    def reset(self):
        return self.blynk.put_pin(self.pins['pause'], '1')

    def red_score(self):
        return self.blynk.get_pin(self.pins['red']['score'])

    def red_alpha(self):
        return self.blynk.get_pin(self.pins['red']['alpha'])

    def red_bravo(self):
        return self.blynk.get_pin(self.pins['red']['bravo'])

    def red_charlie(self):
        return self.blynk.get_pin(self.pins['red']['charlie'])

    def yellow_score(self):
        return self.blynk.get_pin(self.pins['yellow']['score'])

    def yellow_alpha(self):
        return self.blynk.get_pin(self.pins['yellow']['alpha'])

    def yellow_bravo(self):
        return self.blynk.get_pin(self.pins['yellow']['bravo'])

    def yellow_charlie(self):
        return self.blynk.get_pin(self.pins['yellow']['charlie'])
