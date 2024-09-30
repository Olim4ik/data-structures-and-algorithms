from .race import Race


class NightElves(Race):

    def __init__(self):
        self.name = "Night Elves"

    def voice(self):
        return "I am an " + str(self)
