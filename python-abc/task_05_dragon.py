#!/usr/bin/python3
"""The Mystical Dragon - Mastering Mixins"""


class SwinMixin:
    """SwinMixin class"""

    def swin(self):
        """print message swin"""
        print("The creature swinms!")


class FlyMixin:
    """FlyMixin class"""

    def fly(self):
        """print message fly"""
        print("The creature flies!")


class Dragon(SwinMixin, FlyMixin):
    """Dragon class"""

    def swim(self):
        """Message print swin"""
        print("The creature swims!")

    def fly(self):
        """Message print fly"""
        print("The creature flies!")

    def roar(self):
        """print message roar"""
        print("The dragon roars!")
