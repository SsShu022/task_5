"""Game"""
KILL_ENEMY = 0
class Character:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

class Enemy(Character):
    """Enemy class"""
    def __init__(self, name, description) -> None:
        super().__init__(name, description)
        self.conversation = None
        self.weakness = None
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
        print(f'{self.name} тут!\n{self.description}')

    def talk(self):
        """"Prints enemy's lines"""
        print(f'[{self.name}] каже: {self.conversation}')

    def fight(self, item):
        """"method that does fight check"""
        if item == self.weakness:
            global KILL_ENEMY
            KILL_ENEMY += 1
            print(f'Ви обійшли {self.name} з {item}.')
            return True
        else:
            return False

    def get_defeated(self):
        """Return info about defeat of character"""
        return KILL_ENEMY

class Friend(Character):
    """Friend class"""
    def __init__(self, name, description) -> None:
        super().__init__(name, description)
        self.conversation = None
        self.character = None
        self.need = None

    def set_conversation(self, conversation):
        """Recieves conversation text"""
        self.conversation = conversation

    def set_character(self, character):
        """Recieves info about friend"""
        self.character = character

    def describe(self):
        """"Prints short info ab friend"""
        print(f'Погляньте! {self.name} тут!\n{self.description}')

    def set_need(self, need):
        """Sets neded for friend"""
        self.need = need

    def give(self, item):
        """Method that implements giving"""
        if item == self.need:
            print(f'О! Це те, що треба! Ви дали {self.name} {item}')
            return True
        return False




    def talk(self):
        """"Prints friend's lines"""
        print(f'[{self.name}] каже: {self.conversation}')

class Item:
    """Item class"""
    def __init__(self, item) -> None:
        self.item = item
        self.description = None

    def set_description(self, description):
        """Gets description of item"""
        self.description = description

    def describe(self):
        """Prints info about item"""
        print(f'[{self.item}] тут - {self.description}')

    def set_item(self, item):
        """Sets item"""
        self.item = item

    def get_name(self):
        """Returns name of the item"""
        return self.item

# class Veapon(Item):
#     pass

# class Support(Item):
#     pass



class Street:
    def __init__(self, street) -> None:
        self.street = street
        self.description = None
        self.sides = []
        self.item = None
        self.character = None

    def set_description(self, description):
        """
        Text goes there
        """
        self.description = description

    def link_street(self, o_street, side):
        """Sets list of lists with info about nearby street/-s"""
        inf = []
        inf.append(o_street)
        inf.append(side)
        self.sides.append(inf)

    def set_character(self, character: Enemy):
        """Sets character"""
        self.character = character

    def set_item(self, item: Item):
        """Sets item"""
        self.item = item

    def get_details(self):
        """"Prints details about street player is in and route to nearby"""
        print(self.street)
        print('--------------------')
        print(self.description)
        l_n = len(self.sides)
        for i in range(l_n):
            print(f'{self.sides[i][0].street} в напрямку: {self.sides[i][1]}')

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
