"""Game"""

class Item:
    """"Class Item"""
    def __init__(self, item) -> None:
        self.item = item
        self.description = None

    def set_description(self, description):
        """Gets description of item"""
        self.description = description

    def describe(self):
        """Prints info about item"""
        print(f'The [{self.item}] is here - {self.description}')

    def set_item(self, item):
        """Sets item"""
        self.item = item

    def get_name(self):
        """Returns name of the item"""
        return self.item

# variable for counting kills
COUNTER = 0

class Enemy:
    """"Class Enemy"""
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None
        self.counter = 0
        self.character = None


    def set_conversation(self, conversation):
        """Recieves conversation text"""
        self.conversation = conversation

    def set_weakness(self, weakness):
        """Recieves"weakness"""
        self.weakness = weakness

    def set_character(self, character):
        """Recieves info about enemy"""
        self.character = character

    def describe(self):
        """"Prints short info ab enemy"""
        print(f'{self.name} is here!\n{self.description}')

    def talk(self):
        """"Prints enemy's lines"""
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, item):
        """"method that does fight check"""
        if item == self.weakness:
            global COUNTER
            COUNTER += 1
            print(f'You fend {self.name} off with the {item}. Counter: {COUNTER}')
            return True
        else:
            return False

    def get_defeated(self):
        """Return info about defeat of character"""
        return COUNTER



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
        """Sets list of lists with info about nw=earby room/-s"""
        inf = []
        inf.append(o_room)
        inf.append(side)
        self.sides.append(inf)

    def set_character(self, character: Enemy):
        """Sets character"""
        self.character = character

    def set_item(self, item: Item):
        """Sets item"""
        self.item = item

    def get_details(self):
        """"Prints details about room player is in and route to nearby"""
        print(self.room)
        print('--------------------')
        print(self.description)
        l_n = len(self.sides)
        for i in range(l_n):
            print(f'The {self.sides[i][0].room} is {self.sides[i][1]}')

    def get_character(self):
        """"Returns character info"""
        return self.character

    def get_item(self):
        """Returns item"""
        return self.item

    def move(self, command):
        """Returns room that locates in given direction"""
        for lst in self.sides:
            if lst[1] == command:
                return lst[0]


class Friend:
    """"Class Friend"""
    def __init__(self, friend) -> None:
        self.friend = friend
