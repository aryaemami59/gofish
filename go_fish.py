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
main_player = {"name": input("What is your name? "), "cards": list(), "books": set()}
john = {"name": "John", "cards": list(), "books": set()}
brandon = {"name": "Brandon", "cards": list(), "books": set()}
jennifer = {"name": "Jennifer", "cards": list(), "books": set()}
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
def collect_books(current_player: dict, rank: str, verb: str, character_name: str):
    current_player['books'].add(rank)
    print(character_name + " now " + verb +  " books of " + '  '.join(sorted(list(current_player['books']))))
    while current_player['cards'].count(rank) != 0:
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
def ran_out_of_cards(current_player: dict, character_name: str):
    for i in fish_pile[:cards_given]:
        current_player['cards'].append(i)
        fish_pile.remove(i)
    print(character_name + " ran out of cards! " + character_name + " got some cards from the fish pile.")
def opponent_gives_card(opponent: dict, current_player: dict, rank: str, character_name: str):
    card_count = 0
    while opponent["cards"].count(rank) != 0:
        current_player['cards'].append(rank)
        opponent["cards"].remove(rank)
        current_player['cards'].sort()
        opponent["cards"].sort()
        card_count += 1
    print(opponent["name"] + " gives " + character_name + " (" + str(card_count) + ") " + rank + "s")
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
                if main_player['cards'].count(rank) != 0:
                    print("You asked " + opponent["name"] + " for: " + rank)
                    if opponent["cards"].count(rank) != 0:
                        opponent_gives_card(opponent, main_player, rank, "You")
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
                if main_player['cards'].count(fished_card) == 4:
                    collect_books(main_player, fished_card, "have", "You")
        else:
            if is_game_over == True:
                break
            print("It is now " + current_player['name'] + "'s turn")
            opponent = dict()
            rank = str()
            other_players = [x for x in players if x != current_player]
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
                    if current_player['cards'].count(rank) == 4:
                        collect_books(current_player, rank, "has", current_player['name'])
                    if len(current_player['cards']) == 0:
                        if len(fish_pile) == 0:
                            game_over()
                            is_game_over = True
                            break
                        elif len(fish_pile) != 0:
                            ran_out_of_cards(current_player, current_player['name'])
                            for i in current_player['cards']:
                                if current_player['cards'].count(i) == 4:
                                    collect_books(current_player, i, "has", current_player['name'])
                elif opponent["cards"].count(rank) == 0:
                    print(opponent["name"] + " does not have " + rank + ".\nIt is now time for " + current_player['name'] + " to Go Fish!")
                    break
            if len(fish_pile) != 0:
                fished_card = going_fishing(current_player, current_player['name'])
                if current_player['cards'].count(fished_card) == 4:
                    collect_books(current_player, fished_card, "has", current_player['name'])
    if is_game_over == False:
        run_game()
run_game()