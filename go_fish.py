import random
import sys

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
while True:
    try:
        player_name: str = input("What is your name? ")
        if len(player_name) not in range(4, 11): raise ValueError
        else: break
    except ValueError:
        print("Your name must be between 4 to 10 characters.")
main_player: dict = {"name": player_name, "cards": list(), "books": set(), "is_eliminated": bool(False)}
john: dict = {"name": "John", "cards": list(), "books": set(), "is_eliminated": bool(False)}
brandon: dict = {"name": "Brandon", "cards": list(), "books": set(), "is_eliminated": bool(False)}
jennifer: dict = {"name": "Jennifer", "cards": list(), "books": set(), "is_eliminated": bool(False)}
players = [main_player, john, brandon, jennifer]
is_game_over = bool(False)
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
def collect_books(current_player: dict, rank: str, verb: str, character_name: str) -> None:
    current_player['books'].add(rank)
    print(character_name + " now " + verb +  " books of " + '  '.join(sorted(list(current_player['books']))))
    while current_player['cards'].count(rank) != 0:
        current_player['cards'].remove(rank)
def game_over() -> None:
    if is_game_over:
        print("Game Over!")
        book_lengths: list[int] = sorted(list())
        for i in players:
            book_lengths.append(len(i['books']))
            print(i['name'] + "'s books: " + "  ".join(sorted(i['books'])))
            print(i['name'] + "'s cards: " + "  ".join(sorted(i['cards'])))
        longest_set = (max(book_lengths))
        print(longest_set)
        winners_list: list[str] = [x['name'] for x in players if len(x['books']) == longest_set]
        print(" and ".join(winners_list) + " has won the game!")
def ran_out_of_cards(current_player: dict, character_name: str) -> None:
    for i in fish_pile[:cards_given]:
        current_player['cards'].append(i)
        fish_pile.remove(i)
    print(character_name + " ran out of cards! " + character_name + " got some cards from the fish pile.")
def opponent_gives_card(opponent: dict, current_player: dict, rank: str, character_name: str) -> None:
    card_count = 0
    while opponent["cards"].count(rank) != 0:
        current_player['cards'].append(rank)
        opponent["cards"].remove(rank)
        current_player['cards'].sort()
        opponent["cards"].sort()
        card_count += 1
    print(opponent["name"] + " gives " + character_name + " (" + str(card_count) + ") " + rank + "s")
def going_fishing(current_player: dict, character_name: str) -> str:
    fished_card = random.choice(fish_pile)
    current_player['cards'].append(fished_card)
    fish_pile.remove(fished_card)
    current_player['cards'].sort()
    print(character_name + " went fishing and caught a " + fished_card)
    return fished_card
def show_cards(current_player: dict) -> None:
    print(current_player['name'] + "'s cards are now:\n" + '  '.join(sorted(current_player['cards'])))
def player_eliminated(current_player: dict, active_players: list) -> None:
    print(current_player['name'] + " has been eliminated!")
    current_player['is_eliminated'] = True
    active_players.remove(current_player)
def main_player_ask(opponent: dict) -> str:
    while True:
        try:
            rank = input("What rank do you want to ask " + opponent["name"] + " for?\n" + "  ".join(sorted(main_player['cards'])) + "\n")
            if rank not in main_player['cards']: raise ValueError
            else: break
        except ValueError: print("You do not have the selected rank")
    print("You asked " + opponent["name"] + " for: " + rank)
    return rank
def choosing_opponent(active_players: list) -> dict:
    if len(active_players) > 2:
        for i in active_players[1:]:
            print(str(active_players.index(i)) + ") " + i['name'])
        while True:
            try:
                which_player = int(input("Which player do you want to ask? "))
                if which_player not in range(1, len(active_players)): raise ValueError
                else:
                    return active_players[which_player]
            except ValueError:
                print("Invalid input.")
    else:
        return active_players[1]
def run_game() -> None:
    opponent = dict()
    rank = str()
    global is_game_over
    active_players = [x for x in players if x['is_eliminated'] == False]
    if len(active_players) < 2:
        is_game_over = bool(True)
    for current_player in active_players:
        if not current_player['cards'] and not fish_pile:
            player_eliminated(current_player, active_players)
            continue
        if not current_player['is_eliminated']:
            if current_player == main_player:
                while True:
                    opponent = choosing_opponent(active_players)
                    show_cards(main_player)
                    rank = main_player_ask(opponent)
                    if rank in opponent["cards"]:
                        opponent_gives_card(opponent, main_player, rank, "You")
                        if not opponent['cards'] and not fish_pile:
                            player_eliminated(opponent, active_players)
                        if main_player['cards'].count(rank) == 4:
                            collect_books(main_player, rank, "have", "You")
                        if not main_player['cards']:
                            if not fish_pile:
                                player_eliminated(main_player, active_players)
                                break
                            elif fish_pile:
                                ran_out_of_cards(main_player, "You")
                                show_cards(main_player)
                                for i in main_player['cards']:
                                    if main_player['cards'].count(i) == 4:
                                        collect_books(main_player, i, "have", "You")
                    elif rank not in opponent["cards"]:
                        print(opponent["name"] + " does not have " + rank + ".\nIt is now time for you to Go Fish!")
                        break
                if main_player['is_eliminated']:
                    continue
                elif fish_pile:
                    fished_card = going_fishing(main_player, "You")
                    if main_player['cards'].count(fished_card) == 4:
                        collect_books(main_player, fished_card, "have", "You")
                elif not fish_pile:
                        print("fish pile is empty")
                        if not main_player['cards'] and len(active_players) > 1:
                            player_eliminated(main_player, active_players)
                        else:
                            continue
            else:
                print("It is now " + current_player['name'] + "'s turn")
                other_players = [x for x in active_players if x != current_player]
                while True:
                    opponent = random.choice(other_players)
                    card: str
                    for card in current_player['cards']:
                        if current_player['cards'].count(card) == 3:
                            rank = card
                        elif current_player['cards'].count(card) == 2:
                            rank = card
                        elif current_player['cards'].count(card) == 1:
                            rank = card
                    print(current_player['name'] + " asked " + opponent['name'] + " for " + rank)
                    if rank in opponent['cards']:
                        opponent_gives_card(opponent, current_player, rank, current_player['name'])
                        if not opponent['cards'] and not fish_pile:
                            player_eliminated(opponent, active_players)
                            other_players.remove(opponent)
                        if current_player['cards'].count(rank) == 4:
                            collect_books(current_player, rank, "has", current_player['name'])
                        if not current_player['cards']:
                            if not fish_pile:
                                player_eliminated(current_player, active_players)
                                break
                            elif fish_pile:
                                ran_out_of_cards(current_player, current_player['name'])
                                for i in current_player['cards']:
                                    if current_player['cards'].count(i) == 4:
                                        collect_books(current_player, i, "has", current_player['name'])
                    elif rank not in opponent["cards"]:
                        print(opponent["name"] + " does not have " + rank + ".\nIt is now time for " + current_player['name'] + " to Go Fish!")
                        break
                if current_player['is_eliminated']:
                    continue
                elif fish_pile:
                    fished_card = going_fishing(current_player, current_player['name'])
                    # if fished_card == rank:
                        
                    if current_player['cards'].count(fished_card) == 4:
                        collect_books(current_player, fished_card, "has", current_player['name'])
                elif not fish_pile:
                    print("fish pile is empty")
                    if not current_player['cards'] and len(active_players) > 1:
                        player_eliminated(current_player, active_players)
                    else:
                        continue
while not is_game_over:
    run_game()
game_over()