#!/usr/bin/pyhton3
""" Abstract Animal Class and its Subclasses"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal Class"""

    def __init__(self):
        """Initialize the Animal class"""
        pass

    @abstractmethod
    def sound(self):
        """Abstract method to return the sound of the animal"""
        pass


class Dog(Animal):
    """Dog class inherit animal"""

    def sound(self):
        """Return sound of dog"""
        return "Bark"


class Cat(Animal):
    """Cat class inherit animal"""

    def sound(self):
        """Return sound of cat"""
        return "Meow"
