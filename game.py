"""Game"""

class Item:
    def __init__(self, item) -> None:
        self.item = item
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f'The [{self.item}] is here - {self.description}')

    def set_item(self, item):
        self.item = item

    def get_name(self):
        return self.item



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
        l_n = len(self.sides)
        for i in range(l_n, -1, -1):
            print(f'The {self.sides[i][0].room} is {self.sides[i][1]}')

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, command):
        for lst in self.sides:
            if lst[1] == command:
                return lst[0]


class Friend:
    def __init__(self, friend) -> None:
        self.friend = friend


class Character:
    pass
