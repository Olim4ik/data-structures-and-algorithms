"""
Dota 2 races:
"""
from abc import ABC, abstractmethod


class Race(ABC):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(Race, cls).__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self, name="Human"):
        if not hasattr(self, '_initialized'):
            self._name = name
            Race._instances[self.__class__] = self
            self._initialized = True

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    @abstractmethod
    def voice(self):
        pass

    @staticmethod
    def race_count():
        return len(Race._instances)

    @classmethod
    def display_all_races(cls):
        for race_cls, race_instance in cls._instances.items():
            print(f"{race_instance.name} is part of {race_cls.__name__}")
