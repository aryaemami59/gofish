import random

spades = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
clubs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
hearts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
diamonds = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
random.shuffle(spades)
random.shuffle(clubs)
random.shuffle(hearts)
random.shuffle(diamonds)
fish_pile = list(spades + clubs + hearts + diamonds)
random.shuffle(fish_pile)
# fish_pile.pop(random.randrange(0:14))
# fish_pile.pop(random.randrange(len(fish_pile)) * 14)
# my_cards = []
# john_cards = []
# random.shuffle(fish_pile);
# for card in fish_pile[:7]:
#     my_cards.append(card)
#     fish_pile.remove(card)
# random.shuffle(fish_pile);
# for card in fish_pile[:7]:
#     john_cards.append(card)
#     fish_pile.remove(card)
# random.shuffle(fish_pile);
# my_cards.sort()
# john_cards.sort()
# for card in fish_pile[:60]:
#     john_cards.append(card)
#     fish_pile.remove(card)
# print(john_cards)
# print(len(john_cards))
# arya = "Arya"
# main_player = input("What is your name? ")
# john = "John"
# brandon = "Brandon"
# jennifer = "Jennifer"
main_player = {"name": input("What is your name? "), "cards": list(), "books": set()}
john = {"name": "John", "cards": list(), "books": set()}
brandon = {"name": "Brandon", "cards": list(), "books": set()}
jennifer = {"name": "Jennifer", "cards": list(), "books": set()}
# opponent = dict()
# my_books = set()
# john_books = set()
# brandon_books = set()
# jennifer_books = set()
players = [main_player, john, brandon, jennifer]
while True:
    try:
        how_many_players = int(input("How many players?\n2\n3\n4\n"))
        if how_many_players not in range(2, 5): raise ValueError
        else: break
    except ValueError:
        print("Invalid input. Please enter a valid number")
amount_of_cards_given = {2: 7, 3: 6, 4: 5}
players = players[:how_many_players]
cards_given = amount_of_cards_given[how_many_players]
for i in players:
    for card in fish_pile[:cards_given]:
        i['cards'].append(card)
        fish_pile.remove(card)
        random.shuffle(fish_pile)
    i['cards'].sort()
# for i in players:
    # for ind, card in enumerate(fish_pile[:cards_given]):
    #     i['cards'].append(fish_pile.pop(ind))
    #     random.shuffle(fish_pile)
    # i['cards'].sort()
# print("Here are your cards:\n", "  ".join(main_player['cards']), "\nIt is your turn")
# if len(players) > 2:
#     for i in players[1:]:
#         print(str(players.index(i)) + ") " + i['name'])
#     while True:
#         try:
#             which_player = int(input("Which player do you want to ask? "))
#             if which_player not in range(1, len(players)): raise ValueError
#             else:
#                 opponent = players[which_player]
#                 break
#         except ValueError:
#             print("Invalid input.")
# else:
#     opponent = players[1]
# while True:
def collect_books(current_player: dict, rank: str, verb: str, character_name: str):
    current_player['books'].add(rank)
    print(character_name + " now " + verb +  " books of " + '  '.join(sorted(list(current_player['books']))))
    while current_player['cards'].count(rank) != 0:
        # current_player['books'].add(current_player['cards'].pop(current_player['cards'].index(rank)))
        current_player['cards'].remove(rank)
        
def game_over():
    print("Game Over!")
    book_lengths = sorted(list())
    for i in players:
        book_lengths.append(i['books'])
    longest_set = max(book_lengths, key=len)
    for j in players:
        if longest_set == j['books']:
            winner = j['name']
            print(winner + " has won the game!")
            break
    # else:
    #     break
def ran_out_of_cards(current_player: dict, character_name: str):
    for i in fish_pile[:cards_given]:
        current_player['cards'].append(i)
        fish_pile.remove(i)
    print(character_name + " ran out of cards! " + character_name + " got some cards from the fish pile.")
    # for ind, card in enumerate(fish_pile[:cards_given]):
    #     main_player['cards'].append(fish_pile.pop(ind))
def opponent_gives_card(opponent: dict, current_player: dict, rank: str, character_name: str):
    card_count = 0
    while opponent["cards"].count(rank) != 0:
        current_player['cards'].append(rank)
        opponent["cards"].remove(rank)
        current_player['cards'].sort()
        opponent["cards"].sort()
        card_count += 1
    print(opponent["name"] + " gives " + character_name + " (" + str(card_count) + ") " + rank + "s")
    # if current_player['cards'].count(rank) == 4:
    #     collect_books(current_player, rank, "have")
    # if len(current_player['cards']) == 0:
    #     if len(fish_pile) == 0:
    #         game_over()
    #         # break
    #     elif len(fish_pile) != 0:
    #         ran_out_of_cards(current_player, "You")
def going_fishing(current_player: dict, character_name: str):
    fished_card = random.choice(fish_pile)
    current_player['cards'].append(fished_card)
    fish_pile.remove(fished_card)
    current_player['cards'].sort()
    print(character_name + " went fishing and caught a " + fished_card)
    return fished_card
def show_cards(character_name: str, character_cards: list):
    print(character_name + "s cards are now:\n" + '  '.join(sorted(character_cards)))
def run_game():
    opponent = dict()
    is_game_over = False
    for current_player in players:
        if current_player == main_player:
            while is_game_over == False:
                if len(players) > 2:
                    for i in players[1:]:
                        print(str(players.index(i)) + ") " + i['name'])
                    while True:
                        try:
                            which_player = int(input("Which player do you want to ask? "))
                            if which_player not in range(1, len(players)): raise ValueError
                            else:
                                opponent = players[which_player]
                                break
                        except ValueError:
                            print("Invalid input.")
                else:
                    opponent = players[1]
                print("Here are your cards:\n", "  ".join(main_player['cards']), "\nIt is your turn")
                while True:
                    try:
                        rank = input("What rank do you want to ask " + opponent["name"] + " for?\n" + "  ".join(sorted(main_player['cards'])) + "\n")
                        if main_player['cards'].count(rank) not in range(1, 4): raise ValueError
                        else: break
                    except ValueError: print("You do not have the selected rank")
                # if main_player['cards'].count(rank) != 0 and main_player['cards'].count(rank) != 4:
                if main_player['cards'].count(rank) != 0:
                    print("You asked " + opponent["name"] + " for: " + rank)
                    if opponent["cards"].count(rank) != 0:
                        opponent_gives_card(opponent, main_player, rank, "You")
                            # card_count = 0
                            # while opponent["cards"].count(rank) != 0:
                            #     # main_player['cards'].append(opponent["cards"].pop(opponent["cards"].index(rank)))
                            #     main_player['cards'].append(rank)
                            #     opponent["cards"].remove(rank)
                            #     main_player['cards'].sort()
                            #     opponent["cards"].sort()
                            #     card_count += 1
                            # else:
                            #     print(opponent["name"] + " gives you (" + str(card_count) + ") " + rank + "s")
                        if main_player['cards'].count(rank) == 4:
                            collect_books(main_player, rank, "have", "You")
                        if len(main_player['cards']) == 0:
                            if len(fish_pile) == 0:
                                game_over()
                                is_game_over = True
                                break
                            elif len(fish_pile) != 0:
                                ran_out_of_cards(main_player, "You")
                                show_cards(main_player['name'], main_player['cards'])
                                for i in main_player['cards']:
                                    if main_player['cards'].count(i) == 4:
                                        collect_books(main_player, i, "have", "You")
                    elif opponent["cards"].count(rank) == 0:
                        print(opponent["name"] + " does not have " + rank + ".\nIt is now time for you to Go Fish!")
                        break
                elif main_player['cards'].count(rank) != 0:
                    print("You do not have the selected rank")
                elif main_player['cards'].count(rank) == 4:
                    print("You already have the full set of this rank!")
            if len(fish_pile) != 0:
                fished_card = going_fishing(main_player, "You")
                # fished_card = random.choice(fish_pile)
                # main_player['cards'].append(fished_card)
                # fish_pile.remove(fished_card)
                # main_player['cards'].sort()
                # print("You went fishing and caught a " + fished_card)
                if main_player['cards'].count(fished_card) == 4:
                    collect_books(main_player, fished_card, "have", "You")
        else:
            if is_game_over == True:
                break
            # This is what happens when the opponent does not have what you asked for. Now you go fish!
            # for current_player in players[1:]:
            print("It is now " + current_player['name'] + "'s turn")
            opponent = dict()
            rank = str()
            other_players = [x for x in players if x != current_player]
            # opponent = random.choice(other_players)
            # for other_player in other_players:
            #     if other_player != current_player:
            #         opponent = other_player
            while is_game_over == False:
                opponent = random.choice(other_players)
                for card in current_player['cards']:
                    if current_player['cards'].count(card) == 3:
                        rank = card
                    elif current_player['cards'].count(card) == 2:
                        rank = card
                    elif current_player['cards'].count(card) == 1:
                        rank = card
                print(current_player['name'] + " asked " + opponent['name'] + " for " + rank)
                if opponent['cards'].count(rank) != 0:
                    opponent_gives_card(opponent, current_player, rank, current_player['name'])
                    # card_count = 0
                    # while opponent['cards'].count(rank) != 0:
                    #     current_player['cards'].append(rank)
                    #     opponent['cards'].remove(rank)
                    #     current_player['cards'].sort()
                    #     opponent['cards'].sort()
                    #     card_count += 1
                    # print(opponent["name"] + " gives " + current_player['name'] + "(" + str(card_count) + ") " + rank + "s")
                    if current_player['cards'].count(rank) == 4:
                        collect_books(current_player, rank, "has", current_player['name'])
                        # current_player['books'].add(rank)
                        # print(current_player['name'] + " now has books of " + "  ".join(sorted(list(current_player['books']))))
                        # while current_player['cards'].count(rank) != 0:
                        #     current_player['cards'].remove(rank)
                    if len(current_player['cards']) == 0:
                        if len(fish_pile) == 0:
                            game_over()
                            is_game_over = True
                            break
                            # print("Game Over!")
                            # book_lengths = sorted(list())
                            # for i in players:
                            #     book_lengths.append(i['books'])
                            # longest_set = max(book_lengths, key=len)
                            # for j in players:
                            #     if longest_set == j['books']:
                            #         winner = j['name']
                            #         print(winner + " has won the game!")
                            #         break
                        elif len(fish_pile) != 0:
                            ran_out_of_cards(current_player, current_player['name'])
                            for i in current_player['cards']:
                                if current_player['cards'].count(i) == 4:
                                    collect_books(current_player, i, "has", current_player['name'])
                            # for i in fish_pile[:cards_given]:
                            #     current_player['cards'].append(i)
                            #     fish_pile.remove(i)
                elif opponent["cards"].count(rank) == 0:
                    print(opponent["name"] + " does not have " + rank + ".\nIt is now time for " + current_player['name'] + " to Go Fish!")
                    break
            if len(fish_pile) != 0:
                fished_card = going_fishing(current_player, current_player['name'])
                # fished_card = random.choice(fish_pile)
                # current_player['cards'].append(fished_card)
                # fish_pile.remove(fished_card)
                # current_player['cards'].sort()
                # print(current_player['name'] + " went fishing and caught a " + fished_card)
                if current_player['cards'].count(fished_card) == 4:
                    collect_books(current_player, fished_card, "has", current_player['name'])
            # if current_player == jennifer:
    # if len(fish_pile) != 0:
        # if is_game_over == True:
        #     break
    if is_game_over == False:
        run_game()
run_game()
# my_cards = ["1", "1", "2", "2", "3", "3", "4"]
# john_cards = ["1", "1", "6", "6", "7", "7", "8"]
# while True:
#     def stage_1(player_1, player_2, player_1_cards, player_2_cards, player_1_books, player_2_books):
#         # while True:
#         while not(len(fish_pile) == 0 and len(player_1_cards) == 0 or len(player_2_cards) == 0):
#             # print(player_2 + "'s cards:\n", "  ".join(player_2_cards))
#             print("Here are " + player_1 + "'s cards:\n", "  ".join(player_1_cards), "\nIt is " + player_1 + "'s turn")
#             rank = input("What rank does " + player_1 + " want to ask " + player_2 + " for?\n" + "  ".join(player_1_cards) + "\n")
#             if player_1_cards.count(rank) != 0 and player_1_cards.count(rank) != 4:
#                 print(player_1 + " asked " + player_2 + " for: \n", rank)
#                 if player_2_cards.count(rank) == 0 and len(fish_pile) != 0:
#                     print(player_2 + " does not have " + rank + ".\nIt is now time for " + player_1 + " to Go Fish!")
#                     break
#                 elif player_2_cards.count(rank) != 0:
#                     card_count = 0
#                     while player_2_cards.count(rank) != 0:
#                         player_1_cards.append(rank)
#                         player_2_cards.remove(rank)
#                         player_1_cards.sort()
#                         player_2_cards.sort()
#                         card_count += 1
#                     else:
#                         print(player_2 + " gives " + player_1 + " ("+ str(card_count)+ ") "+ rank + "s")
#                         print(player_1 + "'s cards are now:\n", "  ".join(player_1_cards))
#                         if player_1_cards.count(rank) == 4:
#                             (player_1_books).add(rank);
#                             books_sorted = list(player_1_books)
#                             books_sorted.sort()
#                             print(player_1 + " now has books of " + '  '.join(books_sorted))
#                             while player_1_cards.count(rank) != 0:
#                                 player_1_cards.remove(rank)
#                             if len(player_1_cards) == 0:
#                                 if len(fish_pile) == 0:
#                                     print("Game Over")
#                                     book_lengths = [player_1_books, player_2_books]
#                                     book_lengths.sort()
#                                     longest_set = max(book_lengths, key=len)
#                                     if longest_set == player_1_books:
#                                         print("The winner is", player_1)
#                                         break
#                                     elif longest_set == player_2_books:
#                                         print("The winner is", player_2)
#                                         break
#                                 elif len(fish_pile) != 0:
#                                     for i in fish_pile[:7]:
#                                         player_1_cards.append(i)
#                                         fish_pile.remove(i)
#             elif player_1_cards.count(rank) == 0:
#                 print(player_1 + " does not have the selected rank")
#             elif player_1_cards.count(rank) == 4:
#                 print(player_1 + " already has the full set of this rank!")
#         if len(fish_pile) != 0:
#             fished_card = random.choice(fish_pile)
#             player_1_cards.append(fished_card)
#             fish_pile.remove(fished_card)
#             player_1_cards.sort()
#             print(player_1 + " went fishing and caught a", fished_card)
#             if player_1_cards.count(fished_card) == 4:
#                 (player_1_books).add(fished_card);
#                 (books_sorted) = list(player_1_books)
#                 books_sorted.sort()
#                 print(player_1 + " now has books of " + '  '.join(books_sorted))
#                 while player_1_cards.count(fished_card) != 0:
#                     player_1_cards.remove(fished_card)
#                 if len(player_1_cards) == 0:
#                     for i in fish_pile[:7]:
#                         player_1_cards.append(i)
#                         fish_pile.remove(i)
#         if len(fish_pile) != 0 and len(player_1_cards) != 0 or len(player_2_cards) != 0:
#             print(player_1 + "'s cards are now:\n", "  ".join(player_1_cards))
#             # print(player_2 + "'s cards are now:\n", "  ".join(player_2_cards))
#     stage_1(main_player, john, my_cards, john_cards, my_books, john_books)
#     # stage_1(john, main_player, john_cards, my_cards, john_books, my_books)
#     if len(fish_pile) == 0 and len(my_cards) == 0 or len(john_cards) == 0:
#         break