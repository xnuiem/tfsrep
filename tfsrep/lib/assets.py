from pprint import pprint

class Assets:

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def generate(self, reports):
        team = type("team", (), {})
        team.name = "Mercury"
        setattr(self, "team", team)
        self.close()
        return self

    def close(self):
        del self.config
        del self.logger




