from race import Race


class Alliance(Race):

    def __init__(self):
        super().__init__("Alliance")

    def voice(self):
        """Override the abstract method in the Race base class"""
        return f"I am an {self}"


# Create instance of Alliance
alliance_race_1 = Alliance()
aliiance_race_2 = Alliance()

print("Alliance 1:", alliance_race_1)
print("Alliance 2:", aliiance_race_2)

print(alliance_race_1 is aliiance_race_2)  # True

# Printing race count and all races
print(f"Total races created: {Race.race_count()}")
Race.display_all_races()
