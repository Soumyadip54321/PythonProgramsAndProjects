#use of dictionary in Python
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0


def score_word(word):
    point_total = 0
    for character in word:
        point_total += letter_to_points.get(character, 0)
    return point_total


def update_point_totals(lst):
    player_to_points = {}
    for player, words in lst.items():
        player_points = 0
        for word in words:
            if word.islower():
                new_word = word.upper()
                word = new_word
            player_points += score_word(word)
        player_to_points[player] = player_points
    print(player_to_points)


player_to_words = {}
player_to_words.update({"player1": ["blue", "tennis", "exit"], "wordNerd": ["EYES", "MACHINE", "EARTH"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMMA", "PERIOD"]})
update_point_totals(player_to_words)



