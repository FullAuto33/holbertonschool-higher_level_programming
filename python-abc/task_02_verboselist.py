#!/usr/bin/python3
"""Extending the Python List with Notifications"""


class VerboseList(list):
    """VerboseList class inherith from list"""

    def append(self, item):
        """Ajoute un item a la liste"""
        super().append(item)
        print("Added {} to the list." .format(item))

    def extend(self, item):
        """Extend the list with multiple items"""
        super().extend(item)
        print("Extended the list with {} items." .format(len(item)))

    def remove(self, item):
        """Supprimer un item de la liste"""
        super().remove(item)
        print("Removed {} from the list." .format(item))

    def pop(self, index=-1):
        """Pop an item from the list"""
        item = super().pop(index)
        print("Popped {} from the list." .format(item))


if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
