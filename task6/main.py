import my_game

centre = my_game.Street("Площа Ринок")
centre.set_description("Центр Львова.")

street = my_game.Street("вул. Лесі Українки")
street.set_description("Вулиця з багатьма хорошими закладами.")

square = my_game.Street("Галицька Площа")
square.set_description("Тут знаходиться пам'ятник Данилу Галицькому; місце зустрічі.")

centre.link_street(street, "південь")
street.link_street(centre, "північ")
street.link_street(square, "захід")
square.link_street(street, "схід")

police = my_game.Enemy("Поліцейський", "Працьовита, але дуже втомлена людина")
police.set_conversation("Виглядаєте підозріло. Покажіть документи, будь ласка")
police.set_weakness("паспорт")
centre.set_character(police)

collegue = my_game.Friend("Максим", "Ваш однокурсник, хороший друг")
collegue.set_conversation("Друже, я загубив десь на площі свої ключі від колегіуму...\nМені кінець")
collegue.set_need("ключі")
square.set_character(collegue)

thief = my_game.Enemy("Злодюжка", "Молодик, що вибрав сумнівний спосіб заробітку")
thief.set_conversation("Добрі гнроші зараз треба...")
thief.set_weakness("брелок")
street.set_character(thief)

# drunkard = my_game.Enemy("П'яничка", "Той самий друг, який ніколи не знає міри...")
# drunkard.set_conversation("Ти! А ну Йди сюди!")
# drunkard.set_weakness("вода")
# square.set_character(drunkard)


ids = my_game.Item("паспорт")
ids.set_description("Те, що ніколи не варто забувати у друга вдома")
square.set_item(ids)

keychain = my_game.Item("брелок")
keychain.set_description("Звичайний брелок, який наспрадві є сигналізацією")
centre.set_item(keychain)

# water = my_game.Item("вода")
# water.set_description("Тамує мпрагу та приаодить до тями в певних ситуаціях")
# street.set_item(water)

key = my_game.Item("ключі")
key.set_description("Знайомі ключі з емблемою колегіуму...")
street.set_item(key)


current_room = centre

backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["північ", "південь", "схід", "захід"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "говорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    # elif command == "дати":
    #     if isinstance(inhabitant, my_game.Friend) is True:
    #         print('Що Ви хочете дати?')
    #         if inhabitant.give() is True:
                
    elif command == "битися":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("Чим Ви захищатиметеся?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with):
                    # What happens if you win?
                    print("Ура!!! Ви виграли!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 3:
                        print("Вітаю, Ви пройшли гру!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Ох, шкода, алк Ви не справилися.")
                    print("Що ж, це кінець")
                    dead = True

            else:
                print("Ви не маєте " + fight_with)
        else:
            print("Ви ще не втрапили в пригоду")
    elif command == "взяти":
        if item is not None:
            print("Ви поклали " + item.get_name() + " у Ваш рюкзак")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Тут нічого нема, щоб щось брати")
    else:
        print("Я не знаю такого: " + command)
