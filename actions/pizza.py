import requests

from st2actions.runners.pythonrunner import Action


class PizzaAction(Action):
    def __init__(self, config=None):
        super(PizzaAction, self).__init__(config=config)

    def run(self):
        return requests.post(
            self.config['pizza']['order_page'],
            data=self.config['pizza']['payload']
        ).text
