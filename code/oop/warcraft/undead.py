from .race import Race


class Undead(Race):

    def __init__(self):
        self.name = "Undead"

    def voice(self):
        return "I am an " + str(self)
