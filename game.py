"""Game"""

class Item:
    def __init__(self, item) -> None:
        self.item = item
        self.description = None

    def set_description(self, description):
        self.description = description

    def set_item(self):
        pass



class Enemy:

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None
        # self.character = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def set_character(self, character):
        self.character = character

    def describe(self):
        print(f'{self.name} is here!\n{self.description}')

    def talk(self):
        print(f'[{self.name} says]: {self.conversation}')

    counter = 0
    def fight(self, item):
        if item == self.weakness:
            self.counter += 1
            print(f'You fend {self.name} off with the {item}')
            return True
        else:
            return False

    def get_defeated(self):
        pass






class Room:
    """
    Class Room
    """
    def __init__(self, room) -> None:
        self.room = room
        self.description = None
        self.sides = []
        self.item = None
        self.character = None

    def set_description(self, description):
        """
        Text goes there
        """
        self.description = description

    def link_room(self, o_room, side):
        inf = []
        inf.append(o_room)
        inf.append(side)
        self.sides.append(inf)

    def set_character(self, character: Enemy):
        self.character = character

    def set_item(self, item: Item):
        self.item = item

    def get_details(self):
        print(self.room)
        print('--------------------')
        print(self.description)
        print(f'The {self.sides[0][0]} is {self.sides[0][1]}')

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, command):
        for lst in self.sides:
            if lst[1] == command:
                return lst[0]






class Friend:
    pass

class Character:
    pass
