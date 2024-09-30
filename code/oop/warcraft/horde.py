
from .race import Race


class Horde(Race):

    def __init__(self):
        self.name = "Horde"

    def voice(self):
        return "I am a " + str(self)
