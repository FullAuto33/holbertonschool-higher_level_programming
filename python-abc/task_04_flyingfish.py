#!/usr/bin/python3
"""The Enigmatic FlyingFish - Exploring Multiple Inheritance"""


class Fish:
    """Fish class"""

    def swim(self):
        """Simulate swimming"""
        print("The fish is swimming")

    def habitat(self):
        """return habtitat fish"""
        print("The fish lives in water")


class Bird:
    """Bird class"""

    def fly(self):
        """Simulate flying"""
        print("The bird is flying")

    def habitat(self):
        """return habitat bird"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from Fish and Bird"""

    def swim(self):
        """Override swim method"""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly method"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat method"""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())