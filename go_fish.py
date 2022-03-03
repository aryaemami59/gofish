from random import shuffle, choice
import sys

clubs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
spades = clubs.copy()
hearts = clubs.copy()
diamonds = clubs.copy()

fish_pile = list(spades + clubs + hearts + diamonds)
shuffle(fish_pile)
# while True:
#     try:
#         player_name: str = input("What is your name? ")
#         if len(player_name) not in range(4, 11):
#             raise ValueError
#         break
#     except ValueError:
#         print("Your name must be between 4 to 10 characters.")


class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = list()
        self.is_eliminated = bool(False)
        self.books = set()
        # self.other_opponents = [
        #     x for x in game.active_players if x is not self]

    def change_other_opponents(self):
        self.other_opponents = [
            x for x in game.active_players if x is not self]

    def choose_opponent(self):
        self.change_other_opponents()
        self.opponent: Player = choice(self.other_opponents)

    def turn(self):
        if not self.is_eliminated:
            print("It is now " + self.name + "'s turn")
            # self.other_opponents()
            # self.change_other_opponents()
            self.choose_opponent()
            self.choose_rank()
            self.ask_for_rank()
            self.if_opponent_does_not_have_rank()
            self.if_opponent_has_rank()
            # self.collect_books(self.rank)

    def choose_rank(self):
        for card in self.cards:
            if self.cards.count(card) == 3:
                self.rank = card
            elif self.cards.count(card) == 2:
                self.rank = card
            else:
                self.rank = card

    def ask_for_rank(self):
        print(self.name + " asked " + self.opponent.name + " for " + self.rank)

    def if_opponent_has_rank(self):
        if self.rank in self.opponent.cards:
            self.opponent_gives_card()

    def opponent_gives_card(self):
        card_count = int(0)
        while self.opponent.cards.count(self.rank) != 0:
            self.cards.append(self.rank)
            self.opponent.cards.remove(self.rank)
            self.sort_my_cards()
            self.opponent.sort_my_cards()
            card_count += 1
        self.opponent_gives_card_message(card_count)
        self.collect_books(self.rank)
        self.turn()

    def opponent_gives_card_message(self, card_count):
        print(self.opponent.name + " gives " +
              self.name + " (" + str(card_count) + ") " + self.rank + "s")

    def collect_books(self, rank):
        if self.cards.count(rank) == 4:
            self.books.add(rank)
            self.remove_rank(rank)
            self.check_for_elimination()
            self.check_if_out_of_cards()
            self.opponent.check_for_elimination()
            self.opponent.check_if_out_of_cards()

    def check_for_books(self):
        for card in self.cards:
            self.collect_books(card)
        self.check_for_elimination()
        self.check_if_out_of_cards()
        self.opponent.check_for_elimination()
        self.opponent.check_if_out_of_cards()

    def sort_my_cards(self):
        self.cards.sort(key=sort_cards)

    def remove_rank(self, rank):
        while self.cards.count(rank) != 0:
            self.cards.remove(rank)

    def check_for_elimination(self):
        if not self.cards and not fish_pile:
            self.elimination_message()
            self.is_eliminated = True
            game.active_players.remove(self)

    def check_if_out_of_cards(self):
        if not self.cards and fish_pile:
            self.get_cards_from_fish_pile()
            self.got_cards_from_fish_pile_message()

    def get_cards_from_fish_pile(self):
        for card in fish_pile[:self.cards_given]:
            self.cards.append(card)
            fish_pile.remove(card)

    def got_cards_from_fish_pile_message(self):
        print(self.name + " ran out of cards! " + self.name +
              " got some cards from the fish pile.")

    def elimination_message(self):
        print(self.name + " has been eliminated!")

    def if_opponent_does_not_have_rank(self):
        if self.rank not in self.opponent.cards:
            self.opponent_does_not_have_rank_message()
            self.going_fishing()
            self.fish_pile_is_empty()

    def opponent_does_not_have_rank_message(self):
        print(self.opponent.name + " does not have " + self.rank + ".")

    def going_fishing(self):
        if fish_pile:
            self.going_fishing_message()
            fished_card = choice(fish_pile)
            self.cards.append(fished_card)
            fish_pile.remove(fished_card)
            self.sort_my_cards()
            self.collect_books(fished_card)
            self.check_if_fished_card_same_as_rank(fished_card)

    def going_fishing_message(self):
        print("It is now time for " + self.name + " to Go Fish!")

    def check_if_fished_card_same_as_rank(self, fished_card):
        if fished_card == self.rank:
            self.if_fished_card_same_as_rank_message()
            self.turn()
        else:
            self.if_fished_card_not_same_as_rank_message()

    def if_fished_card_same_as_rank_message(self):
        print(self.name + " went fishing and caught a " + self.rank)

    def if_fished_card_not_same_as_rank_message(self):
        print(self.name + " went fishing and did not catch a " + self.rank)

    def fish_pile_is_empty(self):
        if self.cards and not fish_pile:
            self.fish_pile_is_empty_message()

    def fish_pile_is_empty_message(self):
        print("Fish pile is empty")


class MainPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.ask_player_name()

    def ask_player_name(self):
        while True:
            try:
                player_name: str = input("What is your name? ")
                if len(player_name) not in range(4, 11):
                    raise ValueError
                break
            except ValueError:
                print("Your name must be between 4 to 10 characters.")
        self.name = player_name

    def show_cards(self):
        self.sort_my_cards()
        print("Your cards are now:\n" + "  ".join(self.cards))


me = MainPlayer("me")
john = Player("John")
brandon = Player("Brandon")
jennifer = Player("Jennifer")


class Game():
    def __init__(self) -> None:
        self.players: list[Player] = [me, john, brandon, jennifer]
        self.is_game_over = bool(False)
        # self.players = [MainPlayer("me")]

    def how_many_players(self):
        while True:
            try:
                number_of_players = int(input("How many players?\n2\n3\n4\n"))
                if number_of_players not in range(2, 5):
                    raise ValueError
                return number_of_players
            except ValueError:
                print("Invalid input. Please enter a valid number")

    def give_cards(self):
        amount_of_cards_given = {2: 7, 3: 6, 4: 5}
        number_of_players = self.how_many_players()
        self.players = self.players[:number_of_players]
        cards_given = amount_of_cards_given[number_of_players]
        for player in self.players:
            for card in fish_pile[:cards_given]:
                player.cards.append(card)
                fish_pile.remove(card)
                shuffle(fish_pile)
            player.cards.sort(key=sort_cards)
            player.cards_given = cards_given

    def set_active_players(self):
        self.active_players = [x for x in self.players if not x.is_eliminated]

    def check_for_game_over(self):
        self.set_active_players()
        if len(self.active_players) < 2:
            print("Game Over!")
            self.determine_winner()
            self.is_game_over = True

    def determine_winner(self):
        book_lengths: list[int] = sorted(list())
        for player in self.players:
            book_lengths.append(len(player.books))
            print(player.name + "'s books: " +
                  "  ".join(sorted(player.books, key=sort_cards)))
            print(player.name + "'s cards: " + "  ".join(sorted(player.cards)))
        longest_set = max(book_lengths)
        winners_list: list[str] = [
            x.name for x in self.players if len(x.books) == longest_set]
        print(" and ".join(winners_list) + " have won the game!")

    def start_game(self):
        self.give_cards()

    def single_run(self):
        self.set_active_players()
        for player in self.active_players:
            self.set_active_players()
            self.check_for_game_over()
            if self.is_game_over:
                break
            player.turn()
            if player.is_eliminated:
                continue

    def full_run(self):
        self.start_game()
        while not self.is_game_over:
            self.single_run()

    # def
        # main_player: dict = {"name": player_name, "cards": list(
        # ), "books": set(), "is_eliminated": bool(False)}
        # john: dict = {"name": "John", "cards": list(), "books": set(),
        #               "is_eliminated": bool(False)}
        # brandon: dict = {"name": "Brandon", "cards": list(
        # ), "books": set(), "is_eliminated": bool(False)}
        # jennifer: dict = {"name": "Jennifer", "cards": list(
        # ), "books": set(), "is_eliminated": bool(False)}
        # players = [main_player, john, brandon, jennifer]
        # players = list()
is_game_over = bool(False)


def sort_cards(card: str):
    if card == "10":
        return 10
    if card == "j":
        return 11
    if card == "q":
        return 12
    if card == "k":
        return 13
    if card == "a":
        return 14
    else:
        return int(card)


# while True:
#     try:
#         how_many_players = int(input("How many players?\n2\n3\n4\n"))
#         if how_many_players not in range(2, 5):
#             raise ValueError
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid number")
game = Game()
# game.give_cards()
# game.single_run()
game.full_run()
# amount_of_cards_given = {2: 7, 3: 6, 4: 5}
# players = players[:how_many_players]
# cards_given = amount_of_cards_given[how_many_players]
# for i in players:
#     for card in fish_pile[:cards_given]:
#         i['cards'].append(card)
#         fish_pile.remove(card)
#         shuffle(fish_pile)
#     i['cards'].sort()


# def collect_books(current_player: dict, rank: str, verb: str, character_name: str) -> None:
#     current_player['books'].add(rank)
#     print(character_name + " now " + verb + " books of " +
#           '  '.join(sorted(list(current_player['books']))))
#     while current_player['cards'].count(rank) != 0:
#         current_player['cards'].remove(rank)
#     if not current_player['cards'] and not fish_pile:
#         current_player['is_eliminated'] = True
#     elif not current_player['cards'] and fish_pile:
#         ran_out_of_cards(current_player, current_player['name'])


# def game_over() -> None:
#     if is_game_over:
#         print("Game Over!")
#         book_lengths: list[int] = sorted(list())
#         for i in players:
#             book_lengths.append(len(i['books']))
#             print(i['name'] + "'s books: " + "  ".join(sorted(i['books'])))
#             print(i['name'] + "'s cards: " + "  ".join(sorted(i['cards'])))
#         longest_set = (max(book_lengths))
#         winners_list: list[str] = [x['name']
#                                    for x in players if len(x['books']) == longest_set]
#         if len(winners_list) > 1:
#             print(" and ".join(winners_list) + " have won the game!")
#         else:
#             print(" and ".join(winners_list) + " has won the game!")


# def ran_out_of_cards(current_player: dict, character_name: str) -> None:
#     for i in fish_pile[:cards_given]:
#         current_player['cards'].append(i)
#         fish_pile.remove(i)
#     print(character_name + " ran out of cards! " +
#           character_name + " got some cards from the fish pile.")


# def opponent_gives_card(opponent: dict, current_player: dict, rank: str, character_name: str) -> None:
#     card_count = 0
#     while opponent["cards"].count(rank) != 0:
#         current_player['cards'].append(rank)
#         opponent["cards"].remove(rank)
#         current_player['cards'].sort()
#         opponent["cards"].sort()
#         card_count += 1
#     print(opponent["name"] + " gives " + character_name +
#           " (" + str(card_count) + ") " + rank + "s")


# def going_fishing(current_player: dict) -> str:
#     fished_card = choice(fish_pile)
#     current_player['cards'].append(fished_card)
#     fish_pile.remove(fished_card)
#     current_player['cards'].sort()
#     return fished_card


# def show_cards(current_player: dict) -> None:
#     print(current_player['name'] + "'s cards are now:\n" +
#           '  '.join(sorted(current_player['cards'])))


# def player_eliminated(current_player: dict, active_players: list) -> None:
#     print(current_player['name'] + " has been eliminated!")
#     current_player['is_eliminated'] = True
#     active_players.remove(current_player)


# def main_player_ask(opponent: dict) -> str:
#     while True:
#         try:
#             rank = input("What rank do you want to ask " +
#                          opponent["name"] + " for?\n" + "  ".join(sorted(main_player['cards'])) + "\n")
#             if rank not in main_player['cards']:
#                 raise ValueError
#             else:
#                 break
#         except ValueError:
#             print("You do not have the selected rank")
#     print("You asked " + opponent["name"] + " for: " + rank)
#     return rank


# def choosing_opponent(active_players: list) -> dict:
#     if len(active_players) > 2:
#         for i in active_players[1:]:
#             print(str(active_players.index(i)) + ") " + i['name'])
#         while True:
#             try:
#                 which_player = int(input("Which player do you want to ask? "))
#                 if which_player not in range(1, len(active_players)):
#                     raise ValueError
#                 else:
#                     return active_players[which_player]
#             except ValueError:
#                 print("Invalid input.")
#     else:
#         return active_players[1]


# def play_turn(current_player: dict, active_players: list[dict]) -> None:
#     other_players = [x for x in active_players if x != current_player]
#     while True:
#         print("It is now " + current_player['name'] + "'s turn")
#         opponent = choice(other_players)
#         card: str
#         for card in current_player['cards']:
#             if current_player['cards'].count(card) == 3:
#                 rank = card
#             elif current_player['cards'].count(card) == 2:
#                 rank = card
#             elif current_player['cards'].count(card) == 1:
#                 rank = card
#         print(current_player['name'] + " asked " +
#               opponent['name'] + " for " + rank)
#         if rank in opponent['cards']:
#             opponent_gives_card(opponent, current_player,
#                                 rank, current_player['name'])
#             if not opponent['cards'] and not fish_pile:
#                 player_eliminated(opponent, active_players)
#                 other_players.remove(opponent)
#             if current_player['cards'].count(rank) == 4:
#                 collect_books(current_player, rank, "has",
#                               current_player['name'])
#             if not current_player['cards']:
#                 if not fish_pile:
#                     player_eliminated(current_player, active_players)
#                     break
#                 elif fish_pile:
#                     ran_out_of_cards(current_player, current_player['name'])
#                     for i in current_player['cards']:
#                         if current_player['cards'].count(i) == 4:
#                             collect_books(current_player, i, "has",
#                                           current_player['name'])
#         elif rank not in opponent["cards"]:
#             print(opponent["name"] + " does not have " + rank + ".")
#             if fish_pile:
#                 print("It is now time for " +
#                       current_player['name'] + " to Go Fish!")
#                 fished_card = going_fishing(current_player)
#                 if current_player['cards'].count(fished_card) == 4:
#                     collect_books(current_player, fished_card,
#                                   "has", current_player['name'])
#                 if fished_card == rank:
#                     print(
#                         current_player['name'] + " went fishing and caught a " + fished_card + ".")
#                     continue
#                 else:
#                     print(
#                         current_player['name'] + " went fishing and did not catch a " + rank + ".")
#                     break
#             else:
#                 print("Fish pile is empty")
#                 break


# def my_turn(active_players: list[dict]) -> None:
#     while True:
#         print("It is your turn.")
#         opponent = choosing_opponent(active_players)
#         show_cards(main_player)
#         rank = main_player_ask(opponent)
#         if rank in opponent["cards"]:
#             opponent_gives_card(opponent, main_player, rank, "You")
#             if not opponent['cards'] and not fish_pile:
#                 player_eliminated(opponent, active_players)
#             if main_player['cards'].count(rank) == 4:
#                 collect_books(main_player, rank, "have", "You")
#             if not main_player['cards']:
#                 if not fish_pile:
#                     player_eliminated(main_player, active_players)
#                     break
#                 elif fish_pile:
#                     ran_out_of_cards(main_player, "You")
#                     show_cards(main_player)
#                     for i in main_player['cards']:
#                         if main_player['cards'].count(i) == 4:
#                             collect_books(main_player, i, "have", "You")
#         elif rank not in opponent["cards"]:
#             print(opponent["name"] + " does not have " + rank + ".")
#             if fish_pile:
#                 print("It is now time for you to Go Fish!")
#                 fished_card = going_fishing(main_player)
#                 print("You went fishing and caught a " + fished_card + ".")
#                 if main_player['cards'].count(fished_card) == 4:
#                     collect_books(main_player, fished_card, "have", "You")
#                 if fished_card == rank:
#                     continue
#                 else:
#                     break
#             else:
#                 print("Fish pile is empty")
#                 break


# def run_game() -> None:
#     global is_game_over
#     active_players = [x for x in players if x['is_eliminated'] == False]

#     if len(active_players) < 2:
#         is_game_over = bool(True)

#     for current_player in active_players:

#         if not current_player['cards'] and not fish_pile:
#             player_eliminated(current_player, active_players)
#             continue

#         if not current_player['is_eliminated']:

#             if current_player is main_player:
#                 my_turn(active_players)
#             else:
#                 play_turn(current_player, active_players)


# while not is_game_over:
#     run_game()
# game_over()
