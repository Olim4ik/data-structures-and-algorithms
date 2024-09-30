"""
Dota 2 races:
"""
from abc import ABC, abstractmethod


class Race(ABC):
    _instances = {}  # Dictionary to hold singleton instances of subclasses

    def __new__(cls, *args, **kwargs):
        """Overrides the instance creation to ensure only one instance per subclass"""
        if cls not in cls._instances:
            instance = super(Race, cls).__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self, name="Human"):
        if not hasattr(self, '_initialized'):
            self._name = name  # Use _name since we're using a property
            Race._instances[self.__class__] = self  # Ensure this instance is saved
            self._initialized = True  # To ensure __init__ only runs once

    def __str__(self):
        return self.name

    @property
    def name(self):
        """Getter for name property"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter for name property"""
        if isinstance(new_name, str) and new_name:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    @abstractmethod
    def voice(self):
        """Abstract method for voice, must be implemented by subclasses"""
        pass

    @staticmethod
    def race_count():
        """Static method that returns the total number of race instances"""
        return len(Race._instances)

    @classmethod
    def display_all_races(cls):
        """Class method that prints all created race instances"""
        for race_cls, race_instance in cls._instances.items():
            print(f"{race_instance.name} is part of {race_cls.__name__}")
