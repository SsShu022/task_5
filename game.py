"""Game"""

class Item:
    def __init__(self) -> None:
        pass
    def set_description(self):
        pass
    def set_item(self):
        pass

class Room:
    """
    Class Room
    """
    def __init__(self, room) -> None:
        self.room = room
        self.description = None
        self.sides = None
        self.item = None

    def set_description(self, description):
        """
        Text goes there
        """
        self.description = description

    def link_room(self, room, side):
        pass

    def set_character(self):
        pass

    def set_item(self, item: Item):
        self.item = item

    def get_details(self):
        pass

    def get_character(self):
        pass

    def get_item(self):
        pass

    def move(self):
        pass



class Enemy:

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
    def set_conversation(self):
        pass
    def set_weakness(self):
        pass
    def set_character(self):
        pass
    def describe(self):
        pass
    def get_defeated(self):
        pass
    def talk(self):
        pass

    def fight(self):
        pass



class Friend:
    pass

class Character:
    pass
