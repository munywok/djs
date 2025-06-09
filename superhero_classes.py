
# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self._name = name              # Encapsulated attribute
        self._power = power            # Encapsulated attribute
        self._origin = origin          # Encapsulated attribute

    def introduce(self):
        return f"I am {self._name} from {self._origin}, and I have the power of {self._power}!"

    def use_power(self):
        return f"{self._name} uses {self._power} to fight crime!"

# Subclass (inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, max_altitude):
        super().__init__(name, power, origin)
        self._max_altitude = max_altitude  # New attribute for subclass

    # Polymorphism: Override method
    def use_power(self):
        return f"{self._name} soars through the skies and unleashes {self._power} from {self._max_altitude} feet!"

    def fly(self):
        return f"{self._name} is flying at {self._max_altitude} feet!"

# Example usage
if __name__ == "__main__":
    hero1 = Superhero("Shadow Ninja", "Invisibility", "Neo-Tokyo")
    hero2 = FlyingSuperhero("Sky Blaze", "Fire Blast", "Solar City", 5000)

    # Calling methods
    print(hero1.introduce())
    print(hero1.use_power())

    print(hero2.introduce())
    print(hero2.use_power())
    print(hero2.fly())
