from random import shuffle, choice

clubs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
spades = clubs.copy()
hearts = clubs.copy()
diamonds = clubs.copy()

fish_pile = list(spades + clubs + hearts + diamonds)
shuffle(fish_pile)


class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = list()
        self.is_eliminated = bool(False)
        self.books = set()

    def change_other_opponents(self) -> None:
        self.other_opponents = [
            x for x in game.active_players if x is not self]

    def choose_opponent(self) -> None:
        self.change_other_opponents()
        self.opponent: Player = choice(self.other_opponents)

    def turn_message(self) -> None:
        print("It is now " + self.name + "'s turn")

    def turn(self) -> None:
        if not self.is_eliminated:
            self.turn_message()
            self.choose_opponent()
            self.choose_rank()
            self.if_opponent_does_not_have_rank()
            self.if_opponent_has_rank()

    def choose_rank(self) -> None:
        for card in self.cards:
            if self.cards.count(card) == 3:
                self.rank = card
            elif self.cards.count(card) == 2:
                self.rank = card
            else:
                self.rank = card
        self.ask_for_rank()

    def ask_for_rank(self) -> None:
        if self.opponent is not me:
            print(self.name + " asked " +
                  self.opponent.name + " for " + self.rank)
        else:
            print(self.name + " asked You for " + self.rank)

    def if_opponent_has_rank(self) -> None:
        if self.rank in self.opponent.cards:
            self.opponent_gives_card()

    def opponent_gives_card(self) -> None:
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

    def opponent_gives_card_message(self, card_count: int) -> None:
        if self.opponent is not me:
            print(self.opponent.name + " gives " + self.name +
                  " (" + str(card_count) + ") " + self.rank + "s")
        else:
            print("You give " + self.name +
                  " (" + str(card_count) + ") " + self.rank + "s")

    def collect_books(self, rank) -> None:
        if self.cards.count(rank) == 4:
            self.books.add(rank)
            self.collect_books_message()
            self.remove_rank(rank)
            self.check_for_elimination()
            self.check_if_out_of_cards()
            self.opponent.check_for_elimination()
            self.opponent.check_if_out_of_cards()

    def collect_books_message(self) -> None:
        print(self.name + " now has books of " +
              "  ".join(sorted(list(self.books), key=sort_cards)))

    def check_for_books(self) -> None:
        for card in self.cards:
            self.collect_books(card)

    def sort_my_cards(self) -> None:
        self.cards.sort(key=sort_cards)

    def remove_rank(self, rank) -> None:
        while self.cards.count(rank) != 0:
            self.cards.remove(rank)

    def check_for_elimination(self) -> None:
        if not self.cards and not fish_pile:
            self.elimination_message()
            self.is_eliminated = True
            game.set_active_players()

    def check_if_out_of_cards(self) -> None:
        if not self.cards and fish_pile:
            self.out_of_cards_message()
            self.get_cards_from_fish_pile()

    def out_of_cards_message(self) -> None:
        print(self.name + " has run out of cards!")

    def get_cards_from_fish_pile(self) -> None:
        for card in fish_pile[:self.cards_given]:
            self.cards.append(card)
            fish_pile.remove(card)
        self.out_of_cards_message()
        self.got_cards_from_fish_pile_message()

    def got_cards_from_fish_pile_message(self) -> None:
        print(self.name + " got some cards from the fish pile.")

    def elimination_message(self) -> None:
        print(self.name + " has been eliminated!")

    def if_opponent_does_not_have_rank(self) -> None:
        if self.rank not in self.opponent.cards:
            self.opponent_does_not_have_rank_message()
            self.going_fishing()
            self.if_fish_pile_is_empty()

    def opponent_does_not_have_rank_message(self) -> None:
        if self.opponent is not me:
            print(self.opponent.name + " does not have " + self.rank + ".")
        else:
            print("You do not have " + self.rank + ".")

    def going_fishing(self) -> None:
        if fish_pile:
            self.going_fishing_message()
            fished_card = choice(fish_pile)
            self.cards.append(fished_card)
            fish_pile.remove(fished_card)
            self.sort_my_cards()
            self.collect_books(fished_card)
            self.check_if_fished_card_same_as_rank(fished_card)

    def going_fishing_message(self) -> None:
        print("It is now time for " + self.name + " to Go Fish!")

    def check_if_fished_card_same_as_rank(self, fished_card: str) -> None:
        if fished_card == self.rank:
            self.if_fished_card_same_as_rank_message()
            self.turn()
        else:
            self.if_fished_card_not_same_as_rank_message()

    def if_fished_card_same_as_rank_message(self) -> None:
        print(self.name + " went fishing and caught a(n) " + self.rank)

    def if_fished_card_not_same_as_rank_message(self) -> None:
        print(self.name + " went fishing and did not catch a(n) " + self.rank)

    def if_fish_pile_is_empty(self) -> None:
        if self.cards and not fish_pile:
            self.fish_pile_is_empty_message()

    def fish_pile_is_empty_message(self) -> None:
        print("Fish pile is empty")


class MainPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.ask_player_name()

    def ask_player_name(self) -> None:
        while True:
            try:
                player_name: str = input("What is your name? ")
                if len(player_name) not in range(4, 11):
                    raise ValueError
                break
            except ValueError:
                print("Your name must be between 4 to 10 characters.")
        self.name = player_name

    def show_cards(self) -> None:
        self.sort_my_cards()
        print("Your cards are now:\n" + "  ".join(self.cards))

    def choose_opponent(self) -> None:
        self.change_other_opponents()
        if len(self.other_opponents) > 1:
            for opponent in self.other_opponents:
                print(str(self.other_opponents.index(opponent) + 1) + ") " +
                      opponent.name)
            while True:
                try:
                    which_player = int(
                        input("Which player do you want to ask? "))
                    if which_player not in range(
                            1, len(self.other_opponents) + 1):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input.")
            self.opponent = self.other_opponents[which_player - 1]
        else:
            self.opponent = self.other_opponents[0]

    def choose_rank(self) -> None:
        while True:
            try:
                rank = input("What rank do you want to ask " +
                             self.opponent.name + " for?\n" +
                             "  ".join(self.cards) + "\n")
                if rank not in self.cards:
                    raise ValueError
                break
            except ValueError:
                print("You do not have the selected rank")
        print("You asked " + self.opponent.name + " for: " + rank)
        self.rank = rank

    def collect_books_message(self) -> None:
        print("You now have books of " +
              "  ".join(sorted(list(self.books), key=sort_cards)))

    def out_of_cards_message(self) -> None:
        print("You have run out of cards!")

    def got_cards_from_fish_pile_message(self) -> None:
        print("You got some cards from the fish pile.")

    def elimination_message(self) -> None:
        print("You have been eliminated!")

    def going_fishing_message(self) -> None:
        print("It is now time for You to Go Fish!")

    def if_fished_card_same_as_rank_message(self) -> None:
        print("You went fishing and caught a(n) " + self.rank)

    def if_fished_card_not_same_as_rank_message(self) -> None:
        print("You went fishing and did not catch a(n) " + self.rank)

    def turn_message(self) -> None:
        print("It is now your turn")

    def opponent_gives_card_message(self, card_count: int) -> None:
        print(self.opponent.name + " gives You (" +
              str(card_count) + ") " + self.rank + "s")


me = MainPlayer("me")
john = Player("John")
brandon = Player("Brandon")
jennifer = Player("Jennifer")


class Game():
    def __init__(self) -> None:
        self.players: list[Player] = [me, john, brandon, jennifer]
        self.is_game_over = bool(False)

    def how_many_players(self):
        while True:
            try:
                number_of_players = int(input("How many players?\n2\n3\n4\n"))
                if number_of_players not in range(2, 5):
                    raise ValueError
                return number_of_players
            except ValueError:
                print("Invalid input. Please enter a valid number")

    def give_cards(self) -> None:
        amount_of_cards_given: dict[int, int] = {2: 7, 3: 6, 4: 5}
        number_of_players: int = self.how_many_players()
        self.players = self.players[:number_of_players]
        cards_given: int = amount_of_cards_given[number_of_players]
        for player in self.players:
            for card in fish_pile[:cards_given]:
                player.cards.append(card)
                fish_pile.remove(card)
                shuffle(fish_pile)
            player.sort_my_cards()
            player.cards_given = cards_given

    def set_active_players(self) -> None:
        self.active_players = [x for x in self.players if not x.is_eliminated]

    def check_for_game_over(self) -> None:
        self.set_active_players()
        if len(self.active_players) < 2:
            print("Game Over!")
            self.determine_winner()
            self.is_game_over = True

    def determine_winner(self) -> None:
        book_lengths: list[int] = sorted(list(), key=sort_cards)
        for player in self.players:
            book_lengths.append(len(player.books))
            print(player.name + "'s books: " +
                  "  ".join(sorted(player.books, key=sort_cards)))
            print(player.name + "'s cards: " + "  ".join(sorted(player.cards)))
        longest_set = max(book_lengths)
        winners_list: list[str] = [
            x.name for x in self.players if len(x.books) == longest_set]
        print(" and ".join(winners_list) + " have won the game!")

    def single_run(self) -> None:
        self.set_active_players()
        self.check_for_game_over()
        for player in self.active_players:
            self.set_active_players()
            self.check_for_game_over()
            if self.is_game_over:
                break
            player.turn()

    def run_game(self) -> None:
        self.give_cards()
        while not self.is_game_over:
            self.single_run()


def sort_cards(card: str):
    return clubs.index(card)


game = Game()
game.run_game()
